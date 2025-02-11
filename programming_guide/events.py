#!/usr/bin/env python

from pyglet import app
from pyglet.window import Window, key, mouse, event

wnd = Window()


@wnd.event
def on_key_press(symbol, _modifiers):
    if symbol == key.A:
        print('The "A" key was pressed.')
    elif symbol == key.LEFT:
        print("The left arrow key was pressed.")
    elif symbol == key.ENTER:
        print("The enter key was pressed.")


@wnd.event
def on_mouse_press(_x, _y, button, _modifiers):
    if button == mouse.LEFT:
        print("The left mouse button was pressed.")


@wnd.event
def on_draw():
    wnd.clear()


event_logger = event.WindowEventLogger()
wnd.push_handlers(event_logger)


app.run()
