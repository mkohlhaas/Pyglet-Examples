#!/usr/bin/env python

import pyglet as pg
from pyglet.window import Window
from pyglet.text import Label

wnd = Window()
label = Label(
    "Hello, world!",
    font_size=36,
    x=wnd.width // 2,
    y=wnd.height // 2,
    anchor_x="center",
    anchor_y="center",
)


@wnd.event
def on_draw():
    wnd.clear()
    label.draw()


pg.app.run()
