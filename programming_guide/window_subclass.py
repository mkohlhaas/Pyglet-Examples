#!/usr/bin/env python

"""Demonstrates a useful pattern for pyglet applications: subclassing Window."""

from pyglet import app
from pyglet.text import Label
from pyglet.window import Window


class HelloWorldWindow(Window):
    def __init__(self):
        super().__init__()
        self.label = Label(
            "Hello, world!",
            font_size=36,
            x=self.width // 2,
            y=self.height // 2,
            anchor_x="center",
        )

    def on_draw(self):
        self.clear()
        self.label.draw()


if __name__ == "__main__":
    window = HelloWorldWindow()
    app.run()
