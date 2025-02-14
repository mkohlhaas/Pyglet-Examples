from pyglet import resource


def center_image(image):
    """Sets an image's anchor point to its center"""
    image.anchor_x = image.width / 2
    image.anchor_y = image.height / 2


# Tell pyglet where to find the resources
resource.path = ["../resources"]
resource.reindex()

# Load the three main resources and get them to draw centered
player_image = resource.image("player.png")
center_image(player_image)

bullet_image = resource.image("bullet.png")
center_image(bullet_image)

asteroid_image = resource.image("asteroid.png")
center_image(asteroid_image)
