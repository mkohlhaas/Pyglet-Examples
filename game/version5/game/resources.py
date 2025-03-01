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

# The engine flame should not be centered on the ship. Rather, it should be shown
# behind it. To achieve this effect, we just set the anchor point outside the
# image bounds.
engine_image = resource.image("engine_flame.png")
engine_image.anchor_x = int(engine_image.width * 1.5)
engine_image.anchor_y = int(engine_image.height / 2)

# Load the bullet sound _without_ streaming so we can play it more than once at a time
bullet_sound = resource.media("bullet.wav", streaming=False)
