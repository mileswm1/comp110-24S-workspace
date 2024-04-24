"""Define the River class managing an ecosystem of fish and bears."""

__author__ = "730323164"

from exercises.ex09.bear import Bear
from exercises.ex09.fish import Fish


class River:
    """A class representing a river ecosystem."""

    day: int
    fish: list[int]
    bears: list[int]

    def __init__(self, num_fish: int, num_bears: int) -> None:
        """New river with a specified number of fish and bears, starting at day zero."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []

        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self) -> None:
        """Remove old fish."""
        self.fish = [fish for fish in self.fish if fish.age <= 3]
        self.bears = [bear for bear in self.bears if bear.age <= 5]

    def remove_fish(self, amount: int):
        """Remove fish from river."""
        for fish in range(amount):
            if self.fish:
                self.fish.pop(0)
            else:
                break

    def bears_eating(self):
        """Bears eating fish."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)

    def check_hunger(self):
        """Hungry bears die off."""
        surviving_bears: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                surviving_bears.append(bear)
        self.bears = surviving_bears

    def repopulate_fish(self):
        """Repopulating fish."""
        offspring_count = (len(self.fish) // 2) * 4
        for num in range(offspring_count):
            self.fish.append(Fish())

    def repopulate_bears(self):
        """Repopulating bears."""
        offspring_count = len(self.bears) // 2
        for num in range(offspring_count):
            self.bears.append(Bear())

    def view_river(self) -> None:
        """Show river status."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")

    def one_river_day(self):
        """Simulate one river day."""
        self.day += 1

        for bear in self.bears:
            bear.one_day()
        
        for fish in self.fish:
            fish.one_day()
        
        self.bears_eating()
        
        self.check_hunger()
        
        self.check_ages()
        
        self.repopulate_fish()
        
        self.repopulate_bears()
        
        self.view_river()

    def one_river_week(self) -> None:
        """One week in the river's lifecycle."""
        for _ in range(7):
            self.one_river_day()