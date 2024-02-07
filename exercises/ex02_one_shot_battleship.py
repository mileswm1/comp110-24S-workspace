"""EX02 - One Shot Battleship."""

__author__ = "730323164"

grid_size: int = 4
secret_row: int = 3
secret_column: int = 2

row: int = int(input("Guess a row: "))

while row < 1 or row > grid_size:
    row = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))

column: int = int(input("Guess a column: "))

while column < 1 or column > grid_size:
    column = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

if row == secret_row and column == secret_column:
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

if row == secret_row and column == secret_column:
    print("Hit!")
elif column == secret_column:
    print("Close! Correct column, wrong row.")
elif row == secret_row:
    print("Close! Correct row, wrong column.")
else:
    print("Miss!")
