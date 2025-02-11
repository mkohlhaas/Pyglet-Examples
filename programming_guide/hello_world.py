#!/usr/bin/env python

from pyglet import app
from pyglet.text import Label
from pyglet.window import Window

wnd = Window()
label = Label(
    "Hello, world!",
    font_name="Times New Roman",
    font_size=148,
    x=wnd.width // 2,
    y=wnd.height // 2,
    anchor_x="center",
    anchor_y="center",
)


@wnd.event
def on_draw():
    wnd.clear()
    label.draw()


app.run()
