#!/usr/bin/env python

from pyglet import app, clock
from pyglet.graphics import Batch
from pyglet.text import Label
from pyglet.window import Window

from game import load, player
from game.physicalobject import PhysicalObject

# Set up a window.
game_window = Window(800, 600)

main_batch = Batch()

# Set up the two top labels
score_label = Label(
    text="Score: 0",
    x=10,
    y=575,
    batch=main_batch,
)
level_label = Label(
    text="Version 2: Basic Motion",
    x=400,
    y=575,
    anchor_x="center",
    batch=main_batch,
)

# Initialize the player sprite.
player_ship: PhysicalObject = player.Player(x=400, y=300, batch=main_batch)


# Make three asteroids so we have something to shoot at.
asteroids = load.asteroids(3, player_ship.position, main_batch)

# Store all objects that update each frame in a list.
game_objects: list[PhysicalObject] = [player_ship] + asteroids

# Tell the main window that the player object responds to events.
game_window.push_handlers(player_ship)


@game_window.event
def on_draw():
    game_window.clear()
    main_batch.draw()


def update(dt):
    for obj in game_objects:
        obj.update(dt)


if __name__ == "__main__":
    clock.schedule_interval(update, 1 / 120.0)
    app.run()
