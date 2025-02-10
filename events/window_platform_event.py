#!/usr/bin/env python

"""Demonstrates how to handle a platform-specific event not defined in pyglet by subclassing Window.

A message will be printed to stdout when the following events are caught:

On Linux, the window properties are changed.

"""

import pyglet


_have_xlib = False

if pyglet.compat_platform.startswith("linux"):
    _have_xlib = True
    from pyglet.window.xlib import XlibEventHandler, xlib


# Subclass Window
class MyWindow(pyglet.window.Window):
    if _have_xlib:

        @XlibEventHandler(xlib.PropertyNotify)
        def _on_window_property_notify(self, _event):
            print("Property notify.")


if __name__ == "__main__":
    window = MyWindow()
    pyglet.app.run()
