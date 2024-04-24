"""File to define Bear class."""

__author__ = "730323164"


class Bear:
    """Representation of a bear in the river ecosystem."""

    def __init__(self) -> None:
        """Initialize a new bear with age and hunger score set to zero."""
        self.age = 0
        self.hunger_score = 0

    def one_day(self) -> None:
        """Aging the bear by one day and increasing hunger."""
        self.age += 1
        self.hunger_score -= 1

    def eat(self, num_fish: int) -> None:
        """Increasing the bear's hunger score based on the number of fish eaten."""
        self.hunger_score += num_fish