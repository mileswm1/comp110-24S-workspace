"""EX04 - utils."""

__author__ = "730323164"


def all(lst: list[int], num: int) -> bool:
    """All."""
    if not lst:
        return False
    for item in lst:
        if item != num:
            return False
    return True


print(all([1, 2, 3], 1))
print(all([1, 1, 1], 2))
print(all([1, 1, 1], 1))


def max(input: list[int]) -> int:
    """Max."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    max_num = input[0]
    for num in input:
        if num > max_num:
            max_num = num
    return max_num


print(max([99, 2, 34]))
print(max([19, 52, 4]))
print(max([9, 25, 734]))


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Is equal."""
    idx = 0
    if len(list1) != len(list2):
        return False
    while idx < len(list1):
        if list1[idx] != list2[idx]:
            return False
        idx += 1
    return True


print(is_equal([1, 0, 1], [1, 0, 1]))
print(is_equal([1, 1, 0], [1, 0, 1]))


def extend(a: list[int], b: list[int]) -> None:
    """Extend."""
    idx = 0
    while idx < len(b):
        a.append(b[idx])
        idx += 1


a: list[int] = [1, 3, 5]
b: list[int] = [2, 4, 6]
extend(a, b)
print(a)


c: list[int] = [7, 8]
extend(c, b)
print(c)