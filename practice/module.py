"""EX03 - Functional Battleship."""

__author__ = "730323164"

import random

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"


def input_guess(grid_size: int, spec: str) -> int:
    """Function to get input guess."""
    assert spec == "row" or spec == "column"

    guess: int = 0
    if spec == "row":
        guess = int(input("Guess a row: "))
    else:
        guess = int(input("Guess a column: "))
    while guess < 1 or guess > grid_size:
        guess = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))
    return guess


def print_grid(grid_size: int, row: int, column: int, correct: bool) -> None:
    """Function print grid."""
    
    if row == row_input and column == column_input:
        assign: str = RED_BOX
    else:
        assign: str = WHITE_BOX

    row_input: int = 1
    while row_input <= grid_size:
        box: str = ""
        column_input: int = 1
        if row == row_input:
            while column_input <= grid_size:
                if column == column_input:
                    box += assign
                else:
                    box += BLUE_BOX
                column_input += 1
        else:
            while column_input <= grid_size:
                box += BLUE_BOX
                column_input += 1
        print(box)
        row_input += 1
        

def correct_guess(row_input: int, column_input: int, row: int, column: int) -> bool:
    """Function to define correct guess."""
    if row_input == row and column_input == column:
        return True
    else:
        return False
    

def main(grid_size: int, row_input: int, column_input: int) -> None:
    """Function to run main game loop."""
    turns: int = 1
    game_over: bool = False

    while turns <= 5 and not game_over:
        print(f"=== Turn {turns}/{5} ===")
        row: int = input_guess(grid_size, "row")
        column: int = input_guess(grid_size, "column")
        correct: bool = correct_guess(row_input, column_input, row, column)
        print_grid(grid_size, row, column, correct)
        if correct:
            print("Hit!")
            print(f"You won in {turns}/{5} turns!")
            turns += 5
        else:
            print("Miss!")
            if turns == 5:
                print("X/5 - Better luck next time!")
        turns += 1


if __name__ == "__main__":
    grid_size: int = random.randint(3, 5)
    main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))