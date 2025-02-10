#!/usr/bin/env python

from pyglet import app
from pyglet.window import Window

"""Simple example demonstrating how to get the text in the clipboard as well as putting text in the clipboard."""

wnd = Window()
print("Existing Clipboard Text:", wnd.get_clipboard_text())


@wnd.event
def on_key_press(_symbol, _modifiers):
    print("Clipboard changed to: Hello World!")
    wnd.set_clipboard_text("Hello World!")
    print("Clipboard Text:", wnd.get_clipboard_text())


@wnd.event
def on_draw():
    wnd.clear()


app.run()
