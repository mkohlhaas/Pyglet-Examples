from random import randint
from random import random as rnd

from pyglet.sprite import Sprite

from game import asteroid, resources, util
from game.asteroid import Asteroid


def player_lives(num_icons, batch=None) -> list[Sprite]:
    """Generate sprites for player life icons"""
    player_lives = []
    for i in range(num_icons):
        new_sprite = Sprite(
            img=resources.player_image, x=785 - i * 30, y=585, batch=batch
        )
        new_sprite.scale = 0.5
        player_lives.append(new_sprite)
    return player_lives


def asteroids(num_asteroids, player_position, batch=None) -> list[Asteroid]:
    """Generate asteroid objects with random positions and velocities, not close to the player"""
    asteroids = []
    for i in range(num_asteroids):
        asteroid_x, asteroid_y, _ = player_position
        while util.distance((asteroid_x, asteroid_y), player_position) < 100:
            asteroid_x = randint(0, 800)
            asteroid_y = randint(0, 600)
        new_asteroid = asteroid.Asteroid(x=asteroid_x, y=asteroid_y, batch=batch)
        new_asteroid.rotation = randint(0, 360)
        new_asteroid.velocity_x, new_asteroid.velocity_y = (rnd() * 40, rnd() * 40)
        asteroids.append(new_asteroid)
    return asteroids
