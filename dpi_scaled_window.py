#!/usr/bin/env python

import pyglet
from pyglet import app, display, graphics, resource, sprite, text, window
from pyglet.window import Window

pyglet.options["debug_gl"] = False
pyglet.options.dpi_scaling = "scaled"

wnd = Window(800, 600, caption="DPI Test", resizable=True)
batch = graphics.Batch()

print("Window DPI", wnd.dpi, "Window Scale", wnd.scale)

hello_label = text.Label(
    "Hello, world",
    font_name="Times New Roman",
    font_size=36,
    x=wnd.width // 2,
    y=wnd.height // 2,
    anchor_x="center",
    anchor_y="center",
    batch=batch,
    dpi=wnd.dpi,
)

mouse_enter_label = text.Label(
    f"enter: x={0}, y={0}",
    x=10,
    y=110,
    font_size=12,
    dpi=wnd.dpi,
    batch=batch,
)

mouse_leave_label = text.Label(
    f"leave: x={0}, y={0}",
    x=10,
    y=85,
    font_size=12,
    dpi=wnd.dpi,
    batch=batch,
)

mouse_motion_label = text.Label(
    f"motion: x={0}, y={0} dx={0}, dy={0}",
    x=10,
    y=60,
    font_size=12,
    dpi=wnd.dpi,
    batch=batch,
)

mouse_drag_label = text.Label(
    f"drag: x={0}, y={0} dx={0}, dy={0}",
    x=10,
    y=35,
    font_size=12,
    dpi=wnd.dpi,
    batch=batch,
)

mouse_press_label = text.Label(
    f"press: x={0}, y={0}",
    x=10,
    y=10,
    font_size=12,
    dpi=wnd.dpi,
    batch=batch,
)

labels = [
    hello_label,
    mouse_enter_label,
    mouse_leave_label,
    mouse_motion_label,
    mouse_drag_label,
    mouse_press_label,
]

dinosaur = resource.animation("programming_guide/dinosaur.gif")

sprite_dino = sprite.Sprite(dinosaur, x=100, y=140, batch=batch)
if pyglet.options.dpi_scaling != "real":
    sprite_dino.scale = wnd.scale


@wnd.event
def on_draw():
    wnd.clear()
    batch.draw()


@wnd.event
def on_mouse_motion(x, y, dx, dy):
    mouse_motion_label.text = f"motion: x={x:.2f}, y={y:.2f} dx={dx:.2f}, dy={dy:.2f}"


@wnd.event
def on_mouse_press(x, y, _button, _modifier):
    mouse_press_label.text = f"press: x={x:.2f}, y={y:.2f}"


@wnd.event
def on_mouse_enter(x, y):
    mouse_enter_label.text = f"enter: x={x:.2f}, y={y:.2f}"


@wnd.event
def on_mouse_leave(x, y):
    mouse_leave_label.text = f"leave: x={x:.2f}, y={y:.2f}"


@wnd.event
def on_mouse_drag(x, y, dx, dy, _button, _modifier):
    mouse_drag_label.text = f"drag: x={x:.2f}, y={y:.2f} dx={dx:.2f}, dy={dy:.2f}"


@wnd.event
def on_resize(_width, _height):
    hello_label.position = (wnd.width // 2, wnd.height // 2, 0)


screens = display.get_display().get_screens()
print(f"Number of screens: {len(screens)}")
selected_screen = screens[0]
fullscreen = False


@wnd.event
def on_key_press(symbol, _modifiers):
    global selected_screen, fullscreen  # noqa: PLW0603
    if len(screens) > 1:
        if symbol == window.key._1:
            selected_screen = screens[1]
        elif symbol == window.key._0:
            selected_screen = screens[0]

    if symbol == window.key.SPACE:
        wnd.set_size(500, 300)
    elif symbol == window.key.F:
        wnd.set_fullscreen(fullscreen, screen=selected_screen)
        fullscreen = not fullscreen


@wnd.event
def on_scale(scale, dpi):
    print("--- on scale")
    print("SCALE_X", scale, dpi)
    print("Window Size:", wnd.get_size())
    print("Window Scale Ratio:", wnd.scale)
    print("Window Frame Buffer Size:", wnd.get_framebuffer_size())
    if pyglet.options.dpi_scaling != "real":
        for label in labels:
            label.dpi = dpi
        sprite_dino.scale = wnd.scale


app.run()
