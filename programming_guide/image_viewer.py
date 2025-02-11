#!/usr/bin/env python

from pyglet import app
from pyglet.resource import image
from pyglet.window import Window

wnd = Window()
image = image("kitten.jpg")

print(image.width, image.height)
print(wnd.width, wnd.height)


def center(win, img):
    return (
        win.width // 2 - img.width // 2,
        win.height // 2 - img.height // 2,
    )


@wnd.event
def on_draw():
    wnd.clear()
    image.blit(*center(wnd, image))


app.run()
