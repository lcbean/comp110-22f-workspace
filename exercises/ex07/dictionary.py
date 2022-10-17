"""Ex07 - Dictionary Functions."""

__author__ = "730557892"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Inverts keys and values of a given dictionary."""
    swapped: dict[str, str] = {}
    for key in dictionary:
        if dictionary[key] in swapped:
            raise KeyError("Can't invert duplicate values!")
        swapped[dictionary[key]] = key
    return swapped
        
    
def favorite_color(colors: dict[str, str]) -> str:
    """Returns most frequent color."""
    most_frequent: str = ""
    result: dict[str, int] = {}
    colors_swapped: dict[str, str] = {}
    for color in colors:
        colors_swapped[colors[color]] = color
    for color in colors_swapped:
        if colors_swapped[color] in result: 
            result[color] += 1
        else:
            result[color] = 1
    i: int = 0
    for color in result:
        while result[color] > i:
            most_frequent = color
            i += 1
    return most_frequent


def count(a_list: list[str]) -> dict[str, int]:
    """Returns a dictionary of the number of times each string in the list appears."""
    result: dict[str, int] = {}
    for item in a_list:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result