"""Ex03 - Structured Wordle."""

__author__ = "730557892"


# this function determines whether or not a letter in the user's guess is anywhere else in the secret_word
def contains_char(secret_word: str, single_letter: str) -> bool:
    """Returns True if the letter is anywhere in the user's guess."""
    assert len(single_letter) == 1
    i: int = 0
    result: bool = False
    while i < len(secret_word) and result is False:
        if secret_word[i] == single_letter:
            result = True
        else:
            i += 1
    return result
    

# this function adds green boxes to the string when the letters match exactly, yellow when
# they are contained elsewhere in the secret_word at a different index, which is checked with the contains_char function,
# and white if not at all
# the final string of emojis is returned at the end once the loop is done checking each letter
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
            if contains_char(secret_word, single_letter) is True:
                emoji_result += YELLOW_BOX
            else:
                emoji_result += WHITE_BOX
        i += 1
    return emoji_result 


# this function asks the user for a word that must have the same amount of letters as the secret word
# or else the user will be asked to provide a new one until the words are the same length
def input_guess(expected_length: int) -> str:
    """Returns the user's guess provided it is the correct length according to the secret word."""
    user_guess: str = input(f"Enter a {expected_length} character word: ")
    while len(user_guess) != expected_length:
        user_guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return user_guess


# implements the previous functions
# while the player has tries left (out of 6) and they haven't won the game
# yet, the current guess they are on is displayed, followed by a prompt for a guess with the same
# character length as the secret_word
# the emojified function is called to print a string of emojis dictating if and where letters match
# if the user guesses right, they win, if not, they continue on to the next guess
def main() -> None: 
    """The entrypoint of the program and main game."""
    secret_word: str = "codes"
    expected_length: int = len(secret_word)
    i: int = 1
    win: bool = False
    while i <= 6 and win is False:
        print(f"=== Turn {i}/6 ===")
        user_guess: str = input_guess(expected_length)
        print(emojified(user_guess, secret_word))
        if user_guess == secret_word:
            print(f"You won in {i}/6 turns!")
            win = True
        else:
            i += 1
    if win is False:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()