import math

from pyglet.sprite import Sprite
from pyglet.window import key

from game import bullet, resources
from game.physicalobject import PhysicalObject


class Player(PhysicalObject):
    """Physical object that responds to user input"""

    def __init__(self, *args, **kwargs):
        super().__init__(img=resources.player_image, *args, **kwargs)

        # Create a child sprite to show when the ship is thrusting
        self.engine_sprite = Sprite(img=resources.engine_image, *args, **kwargs)
        self.engine_sprite.visible = False

        # Set some easy-to-tweak constants
        self.thrust = 300.0
        self.rotate_speed = 200.0
        self.bullet_speed = 700.0

        # Player should not collide with own bullets
        self.reacts_to_bullets = False

        # Tell the game handler about any event handlers
        self.key_handler = key.KeyStateHandler()
        self.event_handlers = [self, self.key_handler]

    def update(self, dt):
        # Do all the normal physics stuff
        super().update(dt)

        if self.key_handler[key.LEFT]:
            self.rotation -= self.rotate_speed * dt
        if self.key_handler[key.RIGHT]:
            self.rotation += self.rotate_speed * dt

        if self.key_handler[key.UP]:
            # Note: pyglet's rotation attributes are in "negative degrees"
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

    def on_key_press(self, symbol, _modifiers):
        if symbol == key.SPACE:
            self.fire()

    def fire(self):
        # Note: pyglet's rotation attributes are in "negative degrees"
        angle_radians = -math.radians(self.rotation)

        # Create a new bullet just in front of the player
        ship_radius = self.image.width / 2  # type: ignore
        bullet_x = self.x + math.cos(angle_radians) * ship_radius
        bullet_y = self.y + math.sin(angle_radians) * ship_radius
        new_bullet = bullet.Bullet(bullet_x, bullet_y, batch=self.batch)

        # Give it some speed
        bullet_vx = self.velocity_x + math.cos(angle_radians) * self.bullet_speed
        bullet_vy = self.velocity_y + math.sin(angle_radians) * self.bullet_speed
        new_bullet.velocity_x, new_bullet.velocity_y = bullet_vx, bullet_vy

        # Add it to the list of objects to be added to the game_objects list
        self.new_objects.append(new_bullet)

        # Play the bullet sound
        resources.bullet_sound.play()

    def delete(self):
        # We have a child sprite which must be deleted when this object
        # is deleted from batches, etc.
        self.engine_sprite.delete()
        super().delete()
