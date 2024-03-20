"""Test my garden functions."""

__author__ = "730323164"

from lessons.garden.garden_helpers import add_by_kind
from lessons.garden.garden_helpers import add_by_date
from lessons.garden.garden_helpers import lookup_by_kind_and_date


def test_add_by_kind_end_use() -> None:
    """Plant of specific kind should return that kind."""
    test: dict[str, list[str]] = {"flower": ["marigold"]}
    add_by_kind(test, "flower", "daisy")
    assert test == {"flower": ["marigold", "daisy"]}


def test_add_by_kind_edge_case() -> None:
    """New plant kind should add a new entry in the dictionary."""
    test: dict[str, list[str]] = {}
    add_by_kind(test, "herb", "mint")
    assert test == {"herb": ["mint"]}


def test_add_by_date_use_case() -> None:
    """Plant by month should appear in the existing list."""
    test: dict[str, list[str]] = {"May": ["jasmine"]}
    add_by_date(test, "May", "azzalea")
    assert test == {"May": ["jasmine", "azzalea"]}


def test_add_by_date_edge_case() -> None:
    """New month should create a new entry in the dictionary."""
    test: dict[str, list[str]] = {}
    add_by_date(test, "April", "tulip")
    assert test == {"April": ["tulip"]}


def test_lookup_by_kind_and_date_use_case() -> None:
    """Plants of given kind in given month."""
    test_1: dict[str, list[str]] = {"flower": ["lily", "daisy"]}
    test_2: dict[str, list[str]] = {"May": ["azzalea", "tulip", "lily"]}
    assert lookup_by_kind_and_date(test_1, test_2, "flower", "May") == "flowers to plant in May: ['lily']"


def test_lookup_by_kind_and_date_edge_case() -> None:
    """No plants of given kind in given month."""
    test_1: dict[str, list[str]] = {"flower": ["rose", "hydrangea"]}
    test_2: dict[str, list[str]] = {"May": ["lily", "daisy"]}
    assert lookup_by_kind_and_date(test_1, test_2, "flower", "May") == "No flowers to plant in May."
