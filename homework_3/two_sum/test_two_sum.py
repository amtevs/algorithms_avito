import pytest

from two_sum import two_sum


def test_basic_case():
    assert two_sum([1, 3, 4, 10], 7) == (1, 2)


def test_equal_numbers():
    assert two_sum([5, 5, 1, 4], 10) == (0, 1)


def test_negative_numbers():
    assert two_sum([-3, 7, 5, 10], 4) == (0, 1)


def test_zeroes():
    assert two_sum([0, 4, 0], 0) == (0, 2)


def test_first_and_last_elements():
    assert two_sum([8, 2, 3, -1], 7) == (0, 3)


def test_pair_at_the_end():
    assert two_sum([10, 20, 3, 4], 7) == (2, 3)