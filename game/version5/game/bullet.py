from pyglet import clock

from game import resources
from game.physicalobject import PhysicalObject


class Bullet(PhysicalObject):
    """Bullets fired by the player"""

    def __init__(self, *args, **kwargs):
        super().__init__(resources.bullet_image, *args, **kwargs)

        # Bullets shouldn't stick around forever
        clock.schedule_once(self.die, 0.5)

        # Flag as a bullet
        self.is_bullet = True

    def die(self, _dt):
        self.dead = True
