"""Ex05 Utils."""

__author__ = "730557892"


def only_evens(a_list: list[int]) -> list[int]:
    """Returns only the even numbers of a given list."""
    # initialize the new list to an empty list
    evens: list[int] = list()
    for item in a_list:
        # for loop go through each item in the given list
        # if its remainder when divided by 2 is 0, it's even so is added to new list
        if item % 2 == 0:
            evens.append(item)
    return evens


def concat(list_1: list[int], list_2: list[int]) -> list[int]:
    """Creates a new list containing the first then second list."""
    # the new list is the combination of list 1 and list 2
    combined: list[int] = list_1 + list_2
    return combined


def sub(a_list: list[int], start_index: int, end_index: int) -> list[int]:
    """Returns a list of numbers from a given list between a start and end index, not including that at the end."""
    # new list initialized to empty list
    new_list: list[int] = list()
    # if the start index is positve, i is initialized to its value 
    if start_index >= 0:
        i: int = start_index
        # makes sure that new list starts at the start index, ends before the end index, start index is less than the length of the 
        # given list, and the loop ends once i has reached the length of the given list to avoid IndexError
        while i >= start_index and i < end_index and start_index != len(a_list) and i < len(a_list):
            new_list.append(a_list[i])
            i += 1
    else:
        # if start index is negative, i is initialized to 0 so that it meets the condition 
        # of the while loop where i >= start_index and if the start is negative, the first
        # item in the new list would have to be the first in the given list
        i: int = 0
        # condition of the while loop makes sure that the new list starts at
        # the start_index (or index 0 in this case) and ends before the end_index
        # so as to not include it. Also ensures there is no IndexError by ending 
        # before the length of the list
        while i >= start_index and i < end_index and i < len(a_list):
            # if i meets all the conditions, the item at the given index is added to the new list
            new_list.append(a_list[i])
            i += 1
    return new_list
