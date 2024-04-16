"""CQ08 - Intro To Object Oriented Programming."""

from __future__ import annotations

__author__ = "730323164"


class Point:
    """Initializing point types."""
    x: float
    y: float

    def __init__(self, x_init: float, y_init: float):
        """Initializing x and y points."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        """Scaling original points by a factor."""
        self.x = factor * self.x
        self.y = factor * self.y

    def scale(self, factor: int) -> Point:
        """Mutating scaling method."""
        new_point_x = factor * self.x
        new_point_y = factor * self.y
        return Point(new_point_x, new_point_y)