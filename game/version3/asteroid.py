#!/usr/bin/env python

# import pyglet
from pyglet import app, clock
from pyglet.graphics import Batch
from pyglet.text import Label
from pyglet.window import Window

from game import load, player
from game.physicalobject import PhysicalObject

game_window = Window(800, 600)

main_batch = Batch()

# Set up the two top labels
score_label = Label(text="Score: 0", x=10, y=575, batch=main_batch)
level_label = Label(
    text="Version 3: Basic Collision",
    x=400,
    y=575,
    anchor_x="center",
    batch=main_batch,
)

player_ship = player.Player(x=400, y=300, batch=main_batch)

player_lives = load.player_lives(3, main_batch)

asteroids = load.asteroids(3, player_ship.position, main_batch)

game_objects: list[PhysicalObject] = [player_ship] + asteroids

game_window.push_handlers(player_ship.key_handler)


@game_window.event
def on_draw():
    game_window.clear()
    main_batch.draw()


def update(dt):
    for obj in game_objects:
        obj.update(dt)

    # To avoid handling collisions twice, we employ nested loops of ranges.
    # This method also avoids the problem of colliding an object with itself.
    for i in range(len(game_objects)):
        for j in range(i + 1, len(game_objects)):
            obj_1 = game_objects[i]
            obj_2 = game_objects[j]

            # Make sure the objects haven't already been killed
            if not obj_1.dead and not obj_2.dead:
                if obj_1.collides_with(obj_2):
                    obj_1.handle_collision_with(obj_2)
                    obj_2.handle_collision_with(obj_1)

    # Get rid of dead objects
    for to_remove in [obj for obj in game_objects if obj.dead]:
        # Remove the object from any batches it is a member of
        to_remove.delete()

        # Remove the object from our list
        game_objects.remove(to_remove)


if __name__ == "__main__":
    clock.schedule_interval(update, 1 / 120.0)
    app.run()
