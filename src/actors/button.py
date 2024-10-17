import graphix
from graphix import Window


class Button(graphix.Rectangle):
    def __init__(self, text: str, p1: graphix.Point, p2: graphix.Point):
        graphix.Rectangle.__init__(self, p1, p2)

        mid_pos = graphix.Point((p1.x + p2.x) // 2, (p1.y + p2.y) // 2)
        self.text = graphix.Text(mid_pos, text)

    def draw(self, window: Window) -> None:
        graphix.Rectangle.draw(self, window)
        self.text.draw(window)

    def click(self, point: graphix.Point) -> bool:
        # checks if a click is inside the box

        within_x_boundary = self.get_p1().x < point.x < self.get_p2().x
        within_y_boundary = self.get_p1().y < point.y < self.get_p2().y

        return within_x_boundary and within_y_boundary

    def undraw(self) -> None:
        graphix.Rectangle.undraw(self)
        self.text.undraw()
