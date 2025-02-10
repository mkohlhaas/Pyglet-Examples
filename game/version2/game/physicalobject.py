from pyglet.sprite import Sprite


class PhysicalObject(Sprite):
    """A sprite with physical properties such as velocity."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.velocity_x = 0.0
        self.velocity_y = 0.0

    def _check_bounds(self):
        """Use the classic Asteroids screen wrapping behavior"""

        min_x = -self.image.width / 2  # type: ignore
        min_y = -self.image.height / 2  # type: ignore
        max_x = 800 + self.image.width / 2  # type: ignore
        max_y = 600 + self.image.height / 2  # type: ignore
        if self.x < min_x:
            self.x = max_x
        elif self.x > max_x:
            self.x = min_x
        if self.y < min_y:
            self.y = max_y
        elif self.y > max_y:
            self.y = min_y

    def update(self, dt):
        """This method should be called every frame."""

        self.x += self.velocity_x * dt
        self.y += self.velocity_y * dt

        self._check_bounds()
