"""Mutating functions."""

__author__ = "730323164"


def manual_append(lst: list[int], num: int) -> None:
    """Mannual append."""
    lst.append(num)


a: list[int] = [1, 2, 3]
manual_append(a, 2)
print(a)


def double(lst: list[int]) -> None:
    """Define double."""
    idx = 0
    while idx < len(lst):
        lst[idx] *= 2
        idx += 1


b: list[int] = [1, 2, 3]
double(b)
print(b)