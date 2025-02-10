import math
from random import randint

from pyglet.sprite import Sprite

from . import resources

Point = tuple[float, float, float]


def distance(
    point_1: Point = (0, 0, 0),
    point_2: Point = (0, 0, 0),
):
    """Returns the distance between two points"""
    return math.sqrt((point_1[0] - point_2[0]) ** 2 + (point_1[1] - point_2[1]) ** 2)


def asteroids(num_asteroids: int, player_position: Point) -> list[Sprite]:
    """Generate asteroid objects with random positions and velocities, not too close to the player"""
    asteroids: list[Sprite] = []
    for _ in range(num_asteroids):
        asteroid_x, asteroid_y, _ = player_position
        while distance((asteroid_x, asteroid_y, _), player_position) < 100:
            asteroid_x = randint(0, 800)
            asteroid_y = randint(0, 600)

        new_asteroid = Sprite(
            img=resources.asteroid_image,
            x=asteroid_x,
            y=asteroid_y,
        )
        new_asteroid.rotation = randint(0, 360)
        asteroids.append(new_asteroid)
    return asteroids
