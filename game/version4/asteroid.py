#!/usr/bin/env python

from pyglet import app, clock
from pyglet.graphics import Batch
from pyglet.text import Label
from pyglet.window import Window

from game import load, player

# Set up a window
game_window = Window(800, 600)

main_batch = Batch()

# Set up the two top labels
score_label = Label(text="Score: 0", x=10, y=575, batch=main_batch)
level_label = Label(
    text="Version 4: Bullets and Structure",
    x=400,
    y=575,
    anchor_x="center",
    batch=main_batch,
)

player_ship = player.Player(x=400, y=300, batch=main_batch)

player_lives = load.player_lives(3, main_batch)

asteroids = load.asteroids(3, player_ship.position, main_batch)

game_objects = [player_ship] + asteroids

# Add any specified event handlers to the event handler stack
for obj in game_objects:
    for handler in obj.event_handlers:
        game_window.push_handlers(handler)


@game_window.event
def on_draw():
    game_window.clear()
    main_batch.draw()


def update(dt):
    for i in range(len(game_objects)):
        for j in range(i + 1, len(game_objects)):
            obj_1 = game_objects[i]
            obj_2 = game_objects[j]

            if not obj_1.dead and not obj_2.dead:
                if obj_1.collides_with(obj_2):
                    obj_1.handle_collision_with(obj_2)
                    obj_2.handle_collision_with(obj_1)

    # Let's not modify the list while traversing it
    to_add = []

    for obj in game_objects:
        obj.update(dt)
        to_add.extend(obj.new_objects)
        obj.new_objects = []

    # Get rid of dead objects
    for to_remove in [obj for obj in game_objects if obj.dead]:
        # If the dying object spawned any new objects, add those to the game_objects list later
        to_add.extend(obj.new_objects)

        # Remove the object from any batches it is a member of
        to_remove.delete()

        # Remove the object from our list
        game_objects.remove(to_remove)

    # Add new objects to the list
    game_objects.extend(to_add)


if __name__ == "__main__":
    clock.schedule_interval(update, 1 / 120.0)
    app.run()
