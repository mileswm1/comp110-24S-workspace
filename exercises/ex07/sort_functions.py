"""Functions that implement sorting algorithms."""

__author__ = "730323164"


def insertion_sort(x: list[int]) -> None:
    """Basic insertion sort algorithm. Insert into an already sorted list."""
    sorted_index: int = 0
    while sorted_index < len(x) - 1:
        unsorted_index: int = sorted_index + 1
        is_swapped: bool = False
        while unsorted_index > 0 and x[unsorted_index] < x[unsorted_index - 1]:
            temp: int = x[unsorted_index]
            x[unsorted_index] = x[unsorted_index - 1]
            x[unsorted_index - 1] = temp
            unsorted_index -= 1
            is_swapped = True
        if not is_swapped:
            sorted_index += 1
    return None


def selection_sort(x: list[int]) -> None:
    """Basic selection sort algorithm. Repeatedly find the minimum and swap it."""
    for i in range(len(x)):
        min_idx = i
        for j in range(i + 1, len(x)):
            if x[j] < x[min_idx]:
                min_idx = j
        temp: int = x[i]
        x[i] = x[min_idx]
        x[min_idx] = temp
    return None