from pyglet.resource import image
import pyglet.resource as resource
from pyglet.image import AbstractImage


def center_image(img: AbstractImage):
    """Sets an image's anchor point to its center"""
    img.anchor_x = int(img.width / 2)
    img.anchor_y = int(img.height / 2)


# Tell pyglet where to find the resources
resource.path = ["../resources"]
resource.reindex()

# Load the three main resources and get them to draw centered
player_image = image("player.png")
center_image(player_image)

bullet_image = image("bullet.png")
center_image(bullet_image)

asteroid_image = image("asteroid.png")
center_image(asteroid_image)
