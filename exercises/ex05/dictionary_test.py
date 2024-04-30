"""Dictionary Tests - EX06."""

__author__ = "730323164"

import pytest


from exercises.ex05.dictionary import invert, favorite_color, count, alphabetizer, update_attendance


def test_invert_common() -> None:
    """A dictionary with unique values should be correctly inverted."""
    test: dict[str, str] = {'a': '1', 'b': '2', 'c': '3'}
    assert invert(test) == {'1': 'a', '2': 'b', '3': 'c'}


def test_invert_edge() -> None:
    """An empty dictionary should return an empty dictionary when inverted."""
    test: dict[str, str] = {}
    assert invert(test) == {}


def test_invert_common_two() -> None:
    """Inverting a dictionary with duplicate values should raise a KeyError."""
    test: dict[str, str] = {'a': '1', 'b': '1'}
    with pytest.raises(KeyError):
        invert(test)


def test_favorite_color_common() -> None:
    """The most common color should be returned correctly."""
    test: dict[str, str] = {'Alyssa': 'red', 'Bynres': 'blue', 'Adam': 'red'}
    assert favorite_color(test) == 'red'


def test_favorite_color_common_two() -> None:
    """In case of a tie, the first occurring color in the dictionary should be returned."""
    test: dict[str, str] = {'Alyssa': 'red', 'Bynres': 'blue', 'Adam': 'blue', 'Miles': 'red'}
    assert favorite_color(test) == 'red'


def test_favorite_color_edge() -> None:
    """An empty dictionary should return an empty string for favorite color."""
    test: dict[str, str] = {}
    assert favorite_color(test) == ""


def test_count_common_two() -> None:
    """Elements that appear multiple times should have correct counts."""
    test: list[str] = ['apple', 'banana', 'apple']
    assert count(test) == {'apple': 2, 'banana': 1}


def test_count_common() -> None:
    """A list with a single element should return correct count."""
    test: list[str] = ['apple']
    assert count(test) == {'apple': 1}


def test_count_edge() -> None:
    """An empty list should return an empty dictionary."""
    test: list[str] = []
    assert count(test) == {}


def test_alphabetizer_common() -> None:
    """Words should be grouped by their first letter and listed."""
    test: list[str] = ['frog', 'monkey', 'fish']
    assert alphabetizer(test) == {'f': ['frog', 'fish'], 'm': ['monkey']}


def test_alphabetizer_common_two() -> None:
    """Alphabetizer should be case insensitive."""
    test: list[str] = ['Frog', 'monkey', 'Fish']
    assert alphabetizer(test) == {'f': ['Frog', 'Fish'], 'm': ['monkey']}


def test_alphabetizer_edge() -> None:
    """An empty list should return an empty dictionary."""
    test: list[str] = []
    assert alphabetizer(test) == {}


def test_update_attendance_common() -> None:
    """Adding a new student to an existing day should update the list."""
    test: dict[str, list[str]] = {'2024-04-01': ['Alyssa']}
    update_attendance(test, '2024-04-01', 'Adam')
    assert test == {'2024-04-01': ['Alyssa', 'Adam']}


def test_update_attendance_common_two() -> None:
    """Adding a student to a new day should create a new entry."""
    test: dict[str, list[str]] = {}
    update_attendance(test, '2024-04-01', 'Alyssa')
    assert test == {'2024-04-01': ['Alyssa']}


def test_update_attendance_edge() -> None:
    """Adding an empty name should still append the name to the list."""
    test: dict[str, list[str]] = {'2024-04-01': ['Alyssa']}
    update_attendance(test, '2024-04-01', '')
    assert test == {'2024-04-01': ['Alyssa', '']}