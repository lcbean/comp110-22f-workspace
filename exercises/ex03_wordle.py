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

def input_guess(expected_length: int) -> str:
    """Returns the user's guess provided it is the correct length according to the secret word."""
    letters: int = expected_length
    user_guess: str = input(f"Enter a {letters} character word: ")
    while len(user_guess) != expected_length:
        user_guess = input(f"That was not {letters} chars! Try again: ")
    return user_guess

def main() -> None: 
    """The entrypoint of the program and main game."""
    secret_word: str = "codes"
    expected_length: int = len(secret_word)
    i: int = 1
    win: bool = False
    while i <= 6 and win == False:
        print(f"=== Turn {i}/6 ===")
        user_guess: str = input_guess(expected_length)
        print(emojified(user_guess, secret_word))
        if user_guess == secret_word:
            print(f"You won in {i}/6 turns!")
            win = True
        else:
            i += 1
    if win == False:
        print("X/6 - Sorry, try again tomorrow!")

if __name__ == "__main__":
    main()