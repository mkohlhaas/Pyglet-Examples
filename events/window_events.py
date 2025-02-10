#!/usr/bin/env python

"""Prints all window events to stdout."""

from pyglet import app, window
from pyglet.window import Window

wnd = Window(resizable=True)

# A logger class, which prints events to stdout or to a file:
win_event_logger = window.event.WindowEventLogger()
wnd.push_handlers(win_event_logger)


@wnd.event
def on_draw():
    wnd.clear()


app.run()
