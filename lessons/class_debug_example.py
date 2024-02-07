"""Battleship"""

grid_size: int = 4
secret_row: int = 3
secret_column: int = 2

row_input: int = int(input("Guess a row: "))

while row_input < 1 or row_input > grid_size:
    row_input = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))

column_input: int = int(input("Guess a column: "))

while column_input < 1 or column_input > grid_size:
    column_input = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

#result: str = RED_BOX
#if row_input == secret_row and column_input == secret_column
#else:
    # WHITE_BOX

# if row_input == secret_row and column_input == secret_column:
   # result: str = RED_BOX
# else:
   # result: str = WHITE_BOX

row_counter: int = 1
while row_counter <= grid_size:
    box: str = ""
    column_counter: int = 1
    if row_input == row_counter:
        while column_counter <= grid_size:
            if column_input == column_counter:
                box += result
            else:
                box += BLUE_BOX
            column_counter += 1
    else:
        while column_counter <= grid_size:
            box += BLUE_BOX
            column_counter += 1
    print(box)
    row_counter += 1

if row_input == secret_row and column_input == secret_column:
    print("Hit!")
elif column_input == secret_column:
    print("Close! Correct column, wrong row.")
elif row_input == secret_row:
    print("Close! Correct row, wrong column.")
else:
    print("Miss!")