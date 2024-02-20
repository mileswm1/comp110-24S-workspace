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
    row_input: int = 1
    column_input: int = 1
    assign: str = ""
    
    if correct:
        assign = RED_BOX
    else:
        assign = WHITE_BOX

    while row_input <= grid_size:
        box: str = ""
        if row == row_input:
            column_input = 1
            while column_input <= grid_size:
                if column == column_input:
                    box += assign
                else:
                    box += BLUE_BOX
                column_input += 1
        else:
            column_input = 1
            while column_input <= grid_size:
                box += BLUE_BOX
                column_input += 1
        row_input += 1
        print(box)
        

def correct_guess(secret_row: int, secret_column: int, row: int, column: int) -> bool:
    """Function to define correct guess."""
    if secret_row == row and secret_column == column:
        return True
    else:
        return False
    

def main(grid_size: int, secret_row: int, secret_column: int) -> None:
    """Function to run main game loop."""
    turns: int = 1
    game_over: bool = False

    while turns <= 5 and not game_over:
        print(f"=== Turn {turns}/{5} ===")
        
        row: int = input_guess(grid_size, "row")
        column: int = input_guess(grid_size, "column")
        
        correct: bool = correct_guess(secret_row, secret_column, row, column)
        
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