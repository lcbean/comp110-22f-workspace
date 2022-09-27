"""Utils Test."""

__author__ = "730557892"


from utils import only_evens, concat, sub


def test_only_evens_empty() -> None:
    """Tests for return of an empty list if given list is empty."""
    a_list: list[int] = list()
    assert only_evens(a_list) == []


def test_only_evens_mix() -> None:
    """Tests that only_evens can find the evens if there is a mix of evens and odds."""
    a_list: list[int] = [1, 2, 3]
    assert only_evens(a_list) == [2]


def test_only_evens_with_negatives() -> None:
    """Tests for finding only evens if there are negative included in the list."""
    a_list: list[int] = [1, -1, 2, -2, 3, -3]
    assert only_evens(a_list) == [2, -2]


def test_concat_one_empty_list() -> None:
    """Tests for return of only the given list."""
    list_1: list[int] = list()
    list_2: list[int] = [1, 2, 3]
    assert concat(list_1, list_2) == [1, 2, 3]


def test_concat_multiple_items() -> None:
    """Tests proper output when multiple items in each list."""
    list_1: list[int] = [1, 2, 3, 4, 5]
    list_2: list[int] = [6, 7, 8, 9, 10]
    assert concat(list_1, list_2) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_concat_different_lengths() -> None:
    """Tests proper output when lists are different lengths."""
    list_1: list[int] = [1, 2, 3]
    list_2: list[int] = [4, 5, 6, 7, 8, 9, 10]
    assert concat(list_1, list_2) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_sub_same_start_and_end_index() -> None:
    """Ensures empty list is the result of the start and end index being the same."""
    a_list: list[int] = [1, 2, 3]
    start_index: int = 1
    end_index: int = 1
    assert sub(a_list, start_index, end_index) == []


def test_sub_long_range() -> None:
    """Tests for proper output if start and end indexes are far apart."""
    a_list: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    start_index: int = 0
    end_index: int = 9
    assert sub(a_list, start_index, end_index) == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_sub_short_range() -> None:
    """Tests for proper output if start and end indexes are close together."""
    a_list: list[int] = [1, 2, 3, 4, 5 ,6, 7, 8, 9, 10]
    start_index: int = 0
    end_index: int = 2
    assert sub(a_list, start_index, end_index) == [1, 2]

    