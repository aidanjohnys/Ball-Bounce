import time

import graphix
from actors.ball import Ball
from utils.vector2 import Vector2


def main():
    window = graphix.Window("Ball Demo", 400, 400)
    FPS = 30

    balls = []
    balls.append(Ball(window, Vector2(200, 200), "Blue", 20, 250, 35))

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
            ball.draw(window)

        # Ball should move at same speed no matter the fps
        time_delta = time.time() - time_before_draw


if __name__ == "__main__":
    main()
