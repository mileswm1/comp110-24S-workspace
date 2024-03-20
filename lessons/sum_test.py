"""Test sum functionality."""

from lessons.sum import sum

def test_sum_empty() -> None:
    assert sum([]) == 0