"""Ex04 - Utils."""

__author__ = "730557892"


def all(numbers: list[int], single_number: int) -> bool:
    """Returns a bool that determines whether all the ints in a list are the same as a given int."""
    if len(numbers) == 0:
        return False
    i: int = 0
    all_same: bool = False
    # Works through each index of a list to see if the number matches, if it doesn't at any point, returns False
    # If they match at each index, returns True at the end
    while i < len(numbers):
        if single_number == numbers[i]:
            all_same = True
        else: 
            return False
        i += 1
    return all_same


def max(numbers: list[int]) -> int:
    """Returns the largest number in a list of ints."""
    if len(numbers) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 1
    # Highest number starts out as the first in the list
    highest_number: int = numbers[0]
    while i < len(numbers):
        # If the number at the next index is higher than the current highest number, it becomes the new highest number 
        if numbers[i] > highest_number:
            highest_number = numbers[i]
        else: 
            i += 1
    # The reigning highest number is returned
    return highest_number
        

def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Given two lists of ints, return True if each index is exactly the same."""
    i: int = 0
    not_equal: bool = False
    # If both lists are empty, they match so return True
    if len(list_1) == 0 and len(list_2) == 0:
        return True
    # While i is less than the length of both the lists (in case one is greater than the other) 
    # if the first index of both lists don't match or if their lengths don't match, return False
    # else the indices must match so the loop repeats until either an index ends up not matching
    # or they all end up matching
    while i < len(list_1) and i < len(list_2):
        if list_1[i] != list_2[i] or len(list_1) != len(list_2):
            return False 
        else:
            not_equal = True 
            i += 1
    return not_equal