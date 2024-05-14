"""Recursion practice."""

__author__ = "730323164"


def f(n: int, k: int) -> int:
    """Defining the function f."""
    if n == 0:
        return 0
    else:
        return k + f(n - 1, k)