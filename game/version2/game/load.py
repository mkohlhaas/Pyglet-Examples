import math
from random import randint
from random import random as rnd

from game import resources
from game.physicalobject import PhysicalObject


def _distance(point_1=(0, 0), point_2=(0, 0)):
    """Returns the distance between two points."""
    return math.sqrt((point_1[0] - point_2[0]) ** 2 + (point_1[1] - point_2[1]) ** 2)


def asteroids(num_asteroids: int, player_position, batch=None) -> list[PhysicalObject]:
    """Generate asteroid objects with random positions and velocities, not too close to the player."""
    asteroids = []
    for _ in range(num_asteroids):
        asteroid_x, asteroid_y, _ = player_position
        while _distance((asteroid_x, asteroid_y), player_position) < 100:
            asteroid_x = randint(0, 800)
            asteroid_y = randint(0, 600)

        new_asteroid = PhysicalObject(
            img=resources.asteroid_image,
            x=asteroid_x,
            y=asteroid_y,
            batch=batch,
        )
        new_asteroid.rotation = randint(0, 360)
        new_asteroid.velocity_x, new_asteroid.velocity_y = (rnd() * 40, rnd() * 40)
        asteroids.append(new_asteroid)
    return asteroids
