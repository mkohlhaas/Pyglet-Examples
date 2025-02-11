#!/usr/bin/env python

"""Demonstrates creation of a transparent overlay window in pyglet."""

from pyglet import app
from pyglet.graphics import Batch
from pyglet.shapes import Circle
from pyglet.window import Window

batch = Batch()
window = Window(
    500,
    500,
    style=Window.WINDOW_STYLE_TRANSPARENT,
)
window.set_caption("Transparent Window")

circle = Circle(
    250,
    250,
    100,
    color=(255, 255, 0),
    batch=batch,
)


@window.event
def on_draw():
    window.clear()
    batch.draw()


app.run()
