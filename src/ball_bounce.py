import time
import random

import graphix
from actors.ball import Ball
from actors.button import Button
from utils.vector2 import Vector2


class BallBounce:
    def __init__(self):
        self.window = graphix.Window("Ball Demo", 400, 400)
        self.number_of_balls = 0
        self.ball_speed = 0

    def menu(self) -> None:
        title = graphix.Text(graphix.Point(200, 50), "Ball Bounce Demo")
        title.draw(self.window)

        label1 = graphix.Text(graphix.Point(100, 100), "Number of Balls: ")
        label1.draw(self.window)
        num_of_balls = graphix.Entry(graphix.Point(200, 100), 4)
        num_of_balls.draw(self.window)

        label2 = graphix.Text(graphix.Point(100, 150), "Speed of Balls: ")
        label2.draw(self.window)

        ball_speed = graphix.Entry(graphix.Point(200, 150), 4)
        ball_speed.draw(self.window)

        start_button = Button("Start", graphix.Point(150, 300), graphix.Point(250, 330))
        start_button.draw(self.window)

        while True:
            point = self.window.get_mouse()
            if start_button.click(point):
                break

        # TODO: add some error handling here
        self.number_of_balls = int(num_of_balls.text)
        self.ball_speed = float(ball_speed.text)

        title.undraw()
        label1.undraw()
        label2.undraw()
        num_of_balls.undraw()
        ball_speed.undraw()
        start_button.undraw()

    def simulation(self) -> None:
        FPS = 60

        balls = []

        for i in range(self.number_of_balls):
            color = "#%06x" % random.randint(0, 0xFFFFFF)
            balls.append(
                Ball(
                    self.window,
                    Vector2(200, 200),
                    color,
                    20,
                    self.ball_speed,
                    random.randint(0, 360),
                )
            )

        # Time delta keeps time so that the movement of the ball is consistent no matter what the fps is
        # using time.sleep is a kind of crude way of making a game loop,
        # not sure if there is a proper way to do this with graphix
        time_delta = 0.0
        while True:
            # Main Loop
            time_before_draw = time.time()

            time.sleep(1 / FPS)  # Should prevent cpu from maxing out

            for ball in balls:
                ball.act(time_delta)
                ball.undraw()
                ball.draw(self.window)

            # Ball should move at same speed no matter the fps
            time_delta = time.time() - time_before_draw
