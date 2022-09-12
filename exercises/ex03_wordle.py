"""Ex03 - Structured Wordle."""

__author__ = "730557892"

def contains_char(secret_word: str, single_letter: str) -> bool:
    """Returns True if the letter is anywhere in the user's guess."""
    assert len(single_letter) == 1
    i: int = 0
    result: bool = False
    while i < len(secret_word) and result == False:
        if secret_word[i] == single_letter:
            result = True
        else:
            i += 1
    return result
    

def emojified(user_guess: str, secret_word: str) -> str:
    """Returns green, yellow, or white boxes depending on if and where letters match."""
    assert len(user_guess) == len(secret_word)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    i: int = 0
    emoji_result: str = ""
    while i < len(secret_word):
        if user_guess[i] == secret_word[i]:
            emoji_result += GREEN_BOX
        else:
            single_letter: str = user_guess[i]
            if contains_char(secret_word, single_letter) == True:
                emoji_result += YELLOW_BOX
            else:
                emoji_result += WHITE_BOX
        i += 1
    return emoji_result 
    


            
        

