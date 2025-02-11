#!/usr/bin/env python


from pyglet.window import key, Window, FPSDisplay
from pyglet.graphics import Batch
from pyglet.text import Label
from pyglet import clock, app
from pyglet.shapes import Circle

wnd = Window(vsync=False)
fps_display = FPSDisplay(window=wnd)
batch = Batch()
label = Label(
    "Press any digit to change the FPS. (frame rate = digit * 10)",
    x=10,
    y=50,
    batch=batch,
)

circle = Circle(
    200,
    200,
    25,
    color=(200, 60, 130),
    batch=batch,
)


@wnd.event
def on_key_press(keycode, _mod):
    rates = {
        key._1: 1 / 10,
        key._2: 1 / 20,
        key._3: 1 / 30,
        key._4: 1 / 40,
        key._5: 1 / 50,
        key._6: 1 / 60,
        key._7: 1 / 70,
        key._8: 1 / 80,
        key._9: 1 / 90,
        key._0: 1 / 100,
    }

    if redraw_rate := rates.get(keycode):
        global fps_display
        clock.unschedule(wnd.draw)
        clock.schedule_interval(wnd.draw, redraw_rate)
        fps_display = FPSDisplay(window=wnd)


MOVEMENT_SPEED = 600


@wnd.event
def on_refresh(dt):
    global MOVEMENT_SPEED
    circle.x += MOVEMENT_SPEED * dt

    if circle.x > wnd.width or circle.x < 0:
        MOVEMENT_SPEED = -MOVEMENT_SPEED

    wnd.clear()
    batch.draw()
    fps_display.draw()


clock.schedule_interval(wnd.draw, 1 / 60)
app.run(None)
