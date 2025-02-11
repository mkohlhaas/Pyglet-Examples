from random import random as rnd
from random import randint
from game import resources
from game.physicalobject import PhysicalObject


class Asteroid(PhysicalObject):
    """An asteroid that divides a little before it dies"""

    def __init__(self, *args, **kwargs):
        super().__init__(resources.asteroid_image, *args, **kwargs)

        # Slowly rotate the asteroid as it moves
        self.rotate_speed = rnd() * 100.0 - 50.0

    def update(self, dt):
        super().update(dt)
        self.rotation += self.rotate_speed * dt

    def handle_collision_with(self, other_object):
        super().handle_collision_with(other_object)

        # Superclass handles deadness already
        if self.dead and self.scale > 0.25:
            num_asteroids = randint(2, 3)
            for i in range(num_asteroids):
                new_asteroid = Asteroid(x=self.x, y=self.y, batch=self.batch)
                new_asteroid.rotation = randint(0, 360)
                new_asteroid.velocity_x = rnd() * 70 + self.velocity_x
                new_asteroid.velocity_y = rnd() * 70 + self.velocity_y
                new_asteroid.scale = self.scale * 0.5
                self.new_objects.append(new_asteroid)
