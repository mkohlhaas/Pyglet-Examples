#!/usr/bin/env python

"""
This example shows the KeyStateHandler polling approach when it comes to catching keyboard events.
"""

from pyglet import app, clock
from pyglet.text import Label
from pyglet.window import Window, key

wnd = Window()
label = Label("Press either A, Enter, or Left Arrow", 50, 50, font_size=36)


key_handler = key.KeyStateHandler()
wnd.push_handlers(key_handler)


def update(_dt):
    if key_handler[key.A]:
        label.text = 'The "A" key was pressed'
    elif key_handler[key.LEFT]:
        label.text = 'The "Left Arrow" key was pressed.'
    elif key_handler[key.ENTER]:
        label.text = 'The "Enter" key was pressed.'
    else:
        label.text = "Press either A, Enter, or Left Arrow"


@wnd.event
def on_draw():
    wnd.clear()
    label.draw()


clock.schedule_interval(update, 1 / 60)


if __name__ == "__main__":
    app.run()
