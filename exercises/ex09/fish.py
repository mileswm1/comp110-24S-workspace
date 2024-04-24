"""Define the Fish class."""

__author__ = "730323164"


class Fish:
    """A class representing a fish in a river."""
    
    def __init__(self) -> None:
        """Initializing a new fish with age set to zero."""
        self.age = 0

    def one_day(self) -> None:
        """Simulatimg one day for the fish, aging it by one."""
        self.age += 1