#!/usr/bin/env python

"""Load and display a GIF animation.

Usage::

    animation.py [<filename>]

If the filename is omitted, a sample animation is loaded
"""

import sys

from pyglet import app, gl, resource
from pyglet.image import load_animation
from pyglet.image.atlas import TextureBin
from pyglet.sprite import Sprite
from pyglet.window import Window

if len(sys.argv) > 1:
    animation = load_animation(sys.argv[1])
    animation.add_to_texture_bin(TextureBin())
else:
    animation = resource.animation("dinosaur.gif")

wnd = Window(
    width=animation.get_max_width(),
    height=animation.get_max_height(),
)


@wnd.event
def on_draw():
    wnd.clear()
    sprite.draw()


sprite = Sprite(animation)


# Set window background color to white.
gl.glClearColor(1, 1, 1, 1)


app.run()
