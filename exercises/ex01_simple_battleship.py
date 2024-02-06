"""EX01 - Simple Battleship - A cute step toward Battleship."""

__author__ = "730323164"

user_1_input: int = int(input("Pick a secret boat location between 1 and 4: "))

if user_1_input < 1:
    print(f"Error! {user_1_input} too low!")
    exit()
if user_1_input > 4:
    print(f"Error! {user_1_input} too high!")
    exit()

user_2_input: int = int(input("Guess a number between 1 and 4: "))

if user_2_input < 1:
    print(f"Error! {user_2_input} too low!")
    exit()
if user_2_input > 4:
    print(f"Error! {user_2_input} too high!")
    exit()

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

if user_1_input != user_2_input:
    guess_wrong: str = WHITE_BOX
else:
    guess_right: str = RED_BOX

box: str = ""

if user_1_input == user_2_input and user_2_input == 1:
    box += guess_right
elif user_1_input != user_2_input and user_2_input == 1:
    box += guess_wrong
else:
    box += BLUE_BOX

if user_1_input == user_2_input and user_2_input == 2:
    box += guess_right
elif user_1_input != user_2_input and user_2_input == 2:
    box += guess_wrong
else:
    box += BLUE_BOX

if user_1_input == user_2_input and user_2_input == 3:
    box += guess_right
elif user_1_input != user_2_input and user_2_input == 3:
    box += guess_wrong
else:
    box += BLUE_BOX

if user_1_input == user_2_input and user_2_input == 4:
    box += guess_right
elif user_1_input != user_2_input and user_2_input == 4:
    box += guess_wrong
else:
    box += BLUE_BOX
print(box)

if user_1_input == user_2_input:
    print("Correct! You hit the ship.")
else:
    print("Incorrect! You missed the ship.")
