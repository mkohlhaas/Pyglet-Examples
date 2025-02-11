from pyglet.resource import image
from pyglet import resource


def center_image(image):
    """Sets an image's anchor point to its center"""
    image.anchor_x = image.width / 2
    image.anchor_y = image.height / 2


resource.path = ["../resources"]
resource.reindex()

player_image = image("player.png")
center_image(player_image)

bullet_image = image("bullet.png")
center_image(bullet_image)

asteroid_image = image("asteroid.png")
center_image(asteroid_image)

# The engine flame should not be centered on the ship.
# Rather, it should be shown behind it. To achieve this effect,
# we just set the anchor point outside the image bounds.
engine_image = resource.image("engine_flame.png")
engine_image.anchor_x = int(engine_image.width * 1.5)
engine_image.anchor_y = int(engine_image.height / 2)
