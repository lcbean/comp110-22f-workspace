"""Example implementing a list utility function."""

# Function name: contains
# We will have 2 parameters: needle(str) and haystack(list[str])
# Return type bool
def contains(needle: str, haystack: list[str]) -> bool: 

    # Gameplan: 
    # 1. Start with the first index
    i: int = 0
    while i < len(haystack):
        if haystack[i] == needle:
            return True
        i += 1
    return False
