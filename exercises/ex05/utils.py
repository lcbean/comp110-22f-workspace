"""Ex05 Utils."""

__author__ = "730557892"


def only_evens(a_list: list[int]) -> list[int]:
    """Returns only the even numbers of a given list."""
    evens: list[int] = list()
    for item in a_list:
        if item % 2 == 0:
            evens.append(item)
    return evens


def concat(list_1: list[int], list_2: list[int]) -> list[int]:
    "Creates a new list containing the first then second list."
    combined: list[int] = list_1 + list_2
    return combined


def sub(a_list: list[int], start_index: int, end_index: int) -> list[int]:
    """Returns a list of numbers from a given list between a start and end index, not including that at the end."""
    new_list: list[int] = list()
    i: int = 0
    while i >= start_index and i < end_index:
        if a_list[i] == a_list[start_index] or a_list[i] == a_list[start_index + i]:
            new_list.append(a_list[i])
        i += 1
    return new_list
