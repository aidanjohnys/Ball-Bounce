import math
import random

import graphix
from utils.vector2 import Vector2


class Ball(graphix.Circle):
    def __init__(self, window: graphix.Window, start_position: Vector2, color: str, radius: int, speed: float,
                 direction: float):
        self.position = start_position
        self.window = window

        # the set_position function overrides the internal position of the ball
        # so the initialization is not important here
        # self.position is the true position of the ball

        graphix.Circle.__init__(self, graphix.Point(0, 0), radius)
        self.fill_colour = color

        self.direction = direction
        self.speed = speed

    def act(self, delta: float):
        # print(f"x: {self.position.x} y: {self.position.y} direction: {self.direction}")

        self.position = self.calc_new_position(delta)

        self.set_position()
        self.collision_physics()

    def calc_new_position(self, delta: float):
        # I don't fully understand the maths behind this, but it basically
        # takes your speed and pos and calculates where you should be after
        # an amount of time

        direction_radians = math.radians(self.direction)

        old_x = self.position.x
        old_y = self.position.y

        new_x = old_x + self.speed * delta * math.cos(direction_radians)
        new_y = old_y + self.speed * delta * math.sin(direction_radians)

        return Vector2(new_x, new_y)

    def set_position(self):
        # updates the internal position of the circle
        # accessing protected variables here to change the position
        # I can't find any other way to do this without moving the position relatively

        self._p1._x = self.position.x - self.radius
        self._p1._y = self.position.y - self.radius

        self._p2._x = self.position.x + self.radius
        self._p2._y = self.position.y + self.radius

    def collision_physics(self):
        # checks if ball is against wall
        # if so, sends the ball flying in the opposite direction

        border_wall_x = self.window.width - 1
        border_wall_y = self.window.height - 1

        # Makes sure that the bounces are a bit random
        random_bounce_deg = random.randint(0, 20) - 10

        if self.position.x + self.radius > border_wall_x:
            # Right Bounce
            self.position.x = border_wall_x - 1 - self.radius

            if self.direction > 90:
                self.direction = 90 + self.direction + random_bounce_deg
            else:
                self.direction = 180 + self.direction + random_bounce_deg

        elif self.position.x - self.radius < 0:
            # Left Bounce
            self.position.x = 1 + self.radius

            if self.direction > 270:
                self.direction = 90 + self.direction + random_bounce_deg
            else:
                self.direction = 180 + self.direction + random_bounce_deg

            self.direction = 90 + self.direction + random_bounce_deg

        elif self.position.y + self.radius > border_wall_y:
            # Bottom Bounce
            self.position.y = border_wall_y - 1 - self.radius

            if self.direction > 180:
                self.direction = 90 + self.direction + random_bounce_deg
            else:
                self.direction = 180 + self.direction + random_bounce_deg

        elif self.position.y - self.radius < 0:
            # Top Bounce
            self.position.y = 1 + self.radius

            if 0 < self.direction < 360:
                self.direction = 90 + self.direction + random_bounce_deg
            else:
                self.direction = 180 + self.direction + random_bounce_deg

        self.direction = self.direction % 360
