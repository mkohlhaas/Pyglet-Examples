#!/usr/bin/env python

"""Bounces balls around a window and plays noises.

This is a simple demonstration of how pyglet efficiently manages many sound channels without intervention.
"""

import sys
from random import random as rnd

from pyglet import app, clock
from pyglet.graphics import Batch
from pyglet.resource import image, media
from pyglet.sprite import Sprite
from pyglet.text import Label
from pyglet.window import Window, key

BALL_IMAGE = "ball.png"
BALL_SOUND = "ball.wav"

if len(sys.argv) > 1:
    BALL_SOUND = sys.argv[1]

wnd = Window(640, 480)

sound = media(BALL_SOUND, streaming=False)
balls_batch = Batch()
balls = []
label = Label(
    "Press space to add a ball, backspace to remove.",
    font_size=14,
    x=wnd.width // 2,
    y=10,
    anchor_x="center",
)


class Ball(Sprite):
    ball_image = image(BALL_IMAGE)
    width: int = ball_image.width
    height: int = ball_image.height

    def __init__(self):
        x = rnd() * (wnd.width - self.width)
        y = rnd() * (wnd.height - self.height)

        super().__init__(self.ball_image, x, y, batch=balls_batch)

        self.dx = (rnd() - 0.5) * 1000
        self.dy = (rnd() - 0.5) * 1000

    def update_position(self, dt):
        if self.x <= 0 or self.x + self.width >= wnd.width:
            self.dx *= -1
            sound.play()
        if self.y <= 0 or self.y + self.height >= wnd.height:
            self.dy *= -1
            sound.play()
        self.x += self.dx * dt
        self.y += self.dy * dt

        self.x = min(max(self.x, 0), wnd.width - self.width)
        self.y = min(max(self.y, 0), wnd.height - self.height)


@wnd.event
def on_key_press(symbol, _modifiers):
    if symbol == key.SPACE:
        balls.append(Ball())
    elif symbol == key.BACKSPACE:
        if balls:
            balls.pop()


@wnd.event
def on_draw():
    wnd.clear()
    balls_batch.draw()
    label.draw()


def update(dt):
    for ball in balls:
        ball.update_position(dt)


if __name__ == "__main__":
    clock.schedule_interval(update, 1 / 30.0)
    app.run()
