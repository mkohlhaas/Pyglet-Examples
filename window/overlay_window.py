#!/usr/bin/env python

"""Demonstrates creation of a transparent overlay window in pyglet."""

from pyglet import app
from pyglet.graphics import Batch
from pyglet.shapes import Circle
from pyglet.window import Window

wnd = Window(
    500,
    500,
    # style=Window.WINDOW_STYLE_OVERLAY,
)
wnd.set_caption("Overlay Window")
batch = Batch()

circle = Circle(
    250,
    250,
    100,
    color=(255, 255, 0),
    batch=batch,
)


@wnd.event
def on_draw():
    wnd.clear()
    batch.draw()


app.run()
