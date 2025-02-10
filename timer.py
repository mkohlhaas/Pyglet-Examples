#!/usr/bin/env python

"""A full-screen minute:second timer.  Leave it in charge of your conference lighting talks.

After 1 minute the timer goes red.  This limit is easily adjustable by hacking the source code.

Press spacebar to start, stop and reset the timer.
"""

from pyglet import app, clock
from pyglet.text import Label
from pyglet.window import Window, key

wnd = Window(fullscreen=True)
time_limit = 1


class Timer:
    def __init__(self):
        self.label = Label(
            "00:00",
            font_size=360,
            x=wnd.width // 2,
            y=wnd.height // 2,
            anchor_x="center",
            anchor_y="center",
        )
        self.reset()

    def reset(self):
        self.time = 0
        self.running = False
        self.label.text = "00:00"
        self.label.color = (255, 255, 255, 255)

    def update(self, dt):
        if self.running:
            self.time += dt
            m, s = divmod(self.time, 60)
            self.label.text = f"{round(m):02}:{round(s):02}"
            if m >= time_limit:
                self.label.color = (180, 0, 0, 255)

        wnd.draw(dt=dt)


@wnd.event
def on_key_press(symbol, _modifiers):
    if symbol == key.SPACE:
        if timer.running:
            timer.running = False
        else:
            if timer.time > 0:
                timer.reset()
            else:
                timer.running = True
    elif symbol == key.ESCAPE:
        wnd.close()


@wnd.event
def on_draw():
    wnd.clear()
    timer.label.draw()


timer = Timer()

# Set timer and redraw update rate to 30 FPS
clock.schedule_interval(timer.update, 1 / 30.0)

# Launch the application
app.run()
