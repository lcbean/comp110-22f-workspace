"""Ex07 - Dictionary Test."""

__author__ = "730557892"


import pytest
from exercises.ex07.dictionary import invert, favorite_color, count


with pytest.raises(KeyError):
    my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
    invert(my_dictionary)


def test_invert_empty() -> None:
    """Tests for empty dictionary if given empty dictionary."""
    dictionary: dict[str, str] = {}
    assert invert(dictionary) == {}


def test_invert_long() -> None:
    """Tests for proper invert of longer dictionary."""
    dictionary: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert invert(dictionary) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert_short() -> None:
    """Tests for proper invert of shorter dictionary."""
    dictionary: dict[str, str] = {'apple': 'cat'}
    assert invert(dictionary) == {'cat': 'apple'}


def test_favorite_color_empty() -> None:
    """Tests for empty string if an empty dictionary is provided."""
    colors: dict[str, str] = {}
    assert favorite_color(colors) == ""


def test_favorite_color_normal() -> None:
    """Tests for return of correct color."""
    colors: dict[str, str] = {"Lindsay": "blue", "Bob": "blue", "Sarah": "yellow"}
    assert favorite_color(colors) == "blue"


def test_favorite_color_tie() -> None:
    """Tests that first color is returned if there is a tie."""
    colors: dict[str, str] = {"Lindsay": "blue", "Bob": "blue", "Sarah": "yellow", "Hank": "yellow"}
    assert favorite_color(colors) == "blue"


def test_count_empty() -> None:
    """Tests for return of empty dictionary."""
    a_list: list[str] = ()
    assert count(a_list) == {}


def test_count_short() -> None:
    """Tests for proper return given a short list."""
    a_list: list[str] = ["apples", "oranges", "apples"]
    assert count(a_list) == {"apples": 2, "oranges": 1}


def test_count_long() -> None:
    """Test for proper return given a longer list."""
    a_list: list[str] = ["apples", "oranges", "apples", "kiwis", "strawberries", "kiwis", "apples"]
    assert count(a_list) == {"apples": 3, "oranges": 1, "kiwis": 2, "strawberries": 1}