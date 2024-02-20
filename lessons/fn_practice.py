import random

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

def input_guess(grid_size: int, spec: str) -> int:
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
    for r in range(1, grid_size + 1):
        box = ""
        for c in range(1, grid_size + 1):
            if r == row and c == column:
                box += RED_BOX if correct else WHITE_BOX
            else:
                box += BLUE_BOX
        print(box)

def correct_guess(secret_row: int, secret_column: int, row: int, column: int) -> bool:
    return secret_row == row and secret_column == column
    
def main(grid_size: int, secret_row: int, secret_column: int) -> None:
    turns: int = 1

    while turns <= 5:
        print(f"=== Turn {turns}/5 ===")
        row: int = input_guess(grid_size, "row")
        column: int = input_guess(grid_size, "column")
        correct: bool = correct_guess(secret_row, secret_column, row, column)
        print_grid(grid_size, row, column, correct)
        if correct:
            print("Hit! You won!")
            print(f"You won in {turns}/5 turns!")
            return
        else:
            print("Miss!")
        turns += 1

    print("X/5 - Better luck next time!")

if __name__ == "__main__":
    grid_size: int = 5  # Set grid size to 5 by 5
    secret_row: int = random.randint(1, grid_size)
    secret_column: int = random.randint(1, grid_size)
    main(grid_size, secret_row, secret_column)