"""Dictionary Tests - EX06."""

__author__ = "730323164"

import pytest
from dictionary import invert, favorite_color, count, alphabetizer, update_attendance


def test_invert_common_one():
    """Test that invert raises KeyError when two keys map to the same value."""
    with pytest.raises(KeyError):
        invert({'alyssa': 'byrnes', 'adam': 'byrnes'})


def test_invert_common_two():
    """Test invert with a simple dictionary."""
    assert invert({'alyssa': '1', 'adam': '2'}) == {'1': 'alyssa', '2': 'adam'}


def test_invert_edge():
    """Test invert with an empty dictionary should return empty dictionary."""
    assert invert({}) == {}


def test_favorite_color_common_one():
    """Test favorite_color with typical case."""
    assert favorite_color({'Alyssa': 'red', 'Byrnes': 'blue', 'Adam': 'red'}) == 'red'


def test_favorite_color_common_two():
    """Test favorite_color breaks ties based on the first appearance."""
    assert favorite_color({'Alyssa': 'red', 'Byrnes': 'blue', 'Adam': 'blue', 'Miles': 'red'}) == 'red'


def test_favorite_color_edge():
    """Test favorite_color with empty dictionary returns empty string."""
    assert favorite_color({}) == ""


def test_count_common_one():
    """Test count where elements appear multiple times."""
    assert count(['apple', 'banana', 'apple']) == {'apple': 2, 'banana': 1}


def test_count_common_two():
    """Test count with a single element list."""
    assert count(['apple']) == {'apple': 1}


def test_count_edge():
    """Test count with an empty list returns empty dictionary."""
    assert count([]) == {}


def test_alphabetizer_common_one():
    """Test alphabetizer groups words by their first letter."""
    assert alphabetizer(['apple', 'banana', 'apricot']) == {'a': ['apple', 'apricot'], 'b': ['banana']}


def test_alphabetizer_common_two():
    """Test alphabetizer is case insensitive."""
    assert alphabetizer(['Apple', 'banana', 'Apricot']) == {'a': ['Apple', 'Apricot'], 'b': ['banana']}


def test_alphabetizer_edge():
    """Test alphabetizer with an empty list returns an empty dictionary."""
    assert alphabetizer([]) == {}


def test_update_attendance_common_one():
    """Test update_attendance adds student to existing day."""
    log = {'2024-03-01': ['Alyssa']}
    update_attendance(log, '2024-03-01', 'Adam')
    assert log == {'2024-03-01': ['Alyssa', 'Adam']}


def test_update_attendance_common_two():
    """Test update_attendance adds new day with student."""
    log = {}
    update_attendance(log, '2024-03-01', 'Alyssa')
    assert log == {'2024-03-01': ['Alyssa']}


def test_update_attendance_edge():
    """Test update_attendance handles adding an empty student name."""
    log = {'2024-03-01': ['Alyssa']}
    update_attendance(log, '2024-03-01', '')
    assert log == {'2024-03-01': ['Alyssa', '']}