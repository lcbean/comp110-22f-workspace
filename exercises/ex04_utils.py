"""Ex04 - Utils."""

__author__ = "730557892"

def all(numbers: list[int], single_number: int) -> bool:
    """Returns a bool that determines whether all the ints in a list are the same as a given int."""
    all_same: bool == False
    i: int = 0
    while i < len(numbers):
        if single_number == numbers[i]:
            all_same = True
        else: 
            all_same = False
        i += 1
    return all_same


def max(numbers: list[int]) -> int:
    """Returns the largest number in a list of ints"""
    if len(numbers) == 0:
        raise ValueError("max() arg is an empty list")
    i: int = 1
    highest_number: int = numbers[0]
    while i < len(numbers):
        if numbers[i] > highest_number:
            highest_number = numbers[i]
        else: 
            i += 1
    return highest_number
        

def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Given two lists of ints, return True if each index is exactly the same."""
    i: int = 0
    not_equal: bool = False
    while i < len(list_1) and i < len(list_2):
        if list_1[i] != list_2[i]:
            return False 
        else:
            not_equal = True 
            i += 1
    return not_equal
                
        

