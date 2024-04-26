"""Dictionary - EX05."""

__author__ = "730323164"


def invert(p: dict[str, str]) -> dict[str, str]:
    """Invert keys in dictionary."""
    inverted: dict[str, str] = {}
    for key in p:
        value_of = p[key]
        if value_of in inverted:
            raise KeyError("Duplicate value found.")
        inverted[value_of] = key
    return inverted


def favorite_color(colors: dict[str, str]) -> str:
    """Finds common color."""
    color_count: dict[str, int] = {}
    for name in colors:
        color = colors[name]
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1

    max: int = 0
    for color in color_count:
        if color_count[color] > max:
            max = color_count[color]

    most: list[str] = []
    for color in color_count:
        if color_count[color] == max:
            most.append(color)

    app_first: int = len(colors)
    pop_most: str = ""
    index = 0
    for name in colors:
        color = colors[name]
        if color in most:
            if index < app_first:
                app_first = index
                pop_most = color
        index += 1
    return pop_most


def count(values: list[str]) -> dict[str, int]:
    """Counts frequency."""
    counts: dict[str, int] = {}
    for item in values:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """Alphebetizes first letter."""
    words_alph: dict[str, list[str]] = {}
    for word in words:
        first = word[0].lower()
        if first in words_alph:
            words_alph[first].append(word)
        else:
            words_alph[first] = [word]
    return words_alph


def update_attendance(log: dict[str, list[str]], day: str, student: str) -> None:
    """Updated attendence."""
    if day in log:
        log[day].append(student)
    else:
        log[day] = [student]