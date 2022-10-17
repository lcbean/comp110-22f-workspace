"""Utils Test."""

__author__ = "730557892"


from exercises.ex05.utils import only_evens, concat, sub


# tests for empty list result if the given list is empty
def test_only_evens_empty() -> None:
    """Tests for return of an empty list if given list is empty."""
    a_list: list[int] = list()
    assert only_evens(a_list) == []


# for when there is a mix of odd and even numbers to make sure only evens are returned
def test_only_evens_mix() -> None:
    """Tests that only_evens can find the evens if there is a mix of evens and odds."""
    a_list: list[int] = [1, 2, 3]
    assert only_evens(a_list) == [2]


# makes sure negatives are returned when even
def test_only_evens_with_negatives() -> None:
    """Tests for finding only evens if there are negative included in the list."""
    a_list: list[int] = [1, -1, 2, -2, 3, -3]
    assert only_evens(a_list) == [2, -2]


# if one list is empty, only the one that is given should be returned
def test_concat_one_empty_list() -> None:
    """Tests for return of only the given list."""
    list_1: list[int] = list()
    list_2: list[int] = [1, 2, 3]
    assert concat(list_1, list_2) == [1, 2, 3]


# makes sure the lists are added together in the right order when they
# have multiple items
def test_concat_multiple_items() -> None:
    """Tests proper output when multiple items in each list."""
    list_1: list[int] = [1, 2, 3, 4, 5]
    list_2: list[int] = [6, 7, 8, 9, 10]
    assert concat(list_1, list_2) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# makes sure the function still works when the lists are different lengths
def test_concat_different_lengths() -> None:
    """Tests proper output when lists are different lengths."""
    list_1: list[int] = [1, 2, 3]
    list_2: list[int] = [4, 5, 6, 7, 8, 9, 10]
    assert concat(list_1, list_2) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# if the start and end index are the same and the end index cannot be included
# the new list will be empty
def test_sub_same_start_and_end_index() -> None:
    """Ensures empty list is the result of the start and end index being the same."""
    a_list: list[int] = [1, 2, 3]
    start_index: int = 1
    end_index: int = 1
    assert sub(a_list, start_index, end_index) == []


# makes sure function works when the start and end index range is large
def test_sub_long_range() -> None:
    """Tests for proper output if start and end indexes are far apart."""
    a_list: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    start_index: int = 0
    end_index: int = 9
    assert sub(a_list, start_index, end_index) == [1, 2, 3, 4, 5, 6, 7, 8, 9]


# checks function for when index range is shorter
def test_sub_short_range() -> None:
    """Tests for proper output if start and end indexes are close together."""
    a_list: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    start_index: int = 0
    end_index: int = 2
    assert sub(a_list, start_index, end_index) == [1, 2]


# makes sure the new list includes items up until the end index even
# when start index is negative
def test_sub_negative_start_index() -> None:
    """Tests for proper output if start index is negative."""
    a_list: list[int] = [1, 2, 3]
    start_index: int = -1
    end_index: int = 2
    assert sub(a_list, start_index, end_index) == [1, 2]


# makes sure the function works when the start and end index are within the list
def test_sub_within_range() -> None:
    """Tests for proper output if both start and end indices are within list range."""
    a_list: list[int] = [1, 2, 3, 4]
    start_index: int = 1
    end_index: int = 3
    assert sub(a_list, start_index, end_index) == [2, 3]


# makes sure the function works when end index is longer than its length
# because the while loop should end when i becomes equal to the given list length
def test_sub_end_index_greater_than_list_length() -> None:
    """Tests for proper output if end index is greater than list length."""
    a_list: list[int] = [1, 2, 3]
    start_index: int = 1
    end_index: int = 4
    assert sub(a_list, start_index, end_index) == [2, 3]