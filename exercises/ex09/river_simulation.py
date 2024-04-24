"""Run the river simulation."""

__author__ = "730323164"

from river import River


def main() -> None:
    """Main function to initiate and run the river simulation."""
    my_river = River(num_fish=20, num_bears=5)
    my_river.view_river()
    for _ in range(10):
        my_river.one_river_day()


if __name__ == "__main__":
    main()