"""Summing the elements of a list using different loops."""

__author__ = "730323164"


def w_sum(vals: list[float]) -> float:
    """Function of while loops."""
    total = 0.0
    index = 0
    while index < len(vals):
        total += vals[index]
        index += 1
    return total


print(w_sum([1.1, 0.9, 1.0]))
print(w_sum([]))


def f_sum(vals: list[float]) -> float:
    """Function of for loops."""
    total = 0.0
    for value in vals:
        total += value
    return total


print(f_sum([1.1, 0.9, 1.0]))
print(f_sum([]))


def f_range_sum(vals: list[float]) -> float:
    """Function of for ... in range(...) loops."""
    total = 0.0
    for index in range(len(vals)):
        total += vals[index]
    return total


print(w_sum([1.1, 0.9, 1.0]))
print(w_sum([]))