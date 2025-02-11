import math

from pyglet.sprite import Sprite
from pyglet.window import key

from game import resources
from game.physicalobject import PhysicalObject


class Player(PhysicalObject):
    """Physical object that responds to user input"""

    def __init__(self, *args, **kwargs):
        super().__init__(img=resources.player_image, *args, **kwargs)

        # Create a child sprite to show when the ship is thrusting.
        self.engine_sprite = Sprite(img=resources.engine_image, *args, **kwargs)
        self.engine_sprite.visible = False

        self.thrust = 300.0
        self.rotate_speed = 200.0

        # Let pyglet handle keyboard events for us.
        self.key_handler = key.KeyStateHandler()

    def update(self, dt):
        super().update(dt)

        if self.key_handler[key.LEFT]:
            self.rotation -= self.rotate_speed * dt
        if self.key_handler[key.RIGHT]:
            self.rotation += self.rotate_speed * dt

        if self.key_handler[key.UP]:
            angle_radians = -math.radians(self.rotation)
            force_x = math.cos(angle_radians) * self.thrust * dt
            force_y = math.sin(angle_radians) * self.thrust * dt
            self.velocity_x += force_x
            self.velocity_y += force_y

            self.engine_sprite.rotation = self.rotation
            self.engine_sprite.x = self.x
            self.engine_sprite.y = self.y
            self.engine_sprite.visible = True
        else:
            self.engine_sprite.visible = False

    def delete(self):
        # We have a child sprite which must be deleted when this object
        # is deleted from batches, etc.
        self.engine_sprite.delete()
        super().delete()
