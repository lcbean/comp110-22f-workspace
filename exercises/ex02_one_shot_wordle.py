"""EX02 - One-Shot Wordle."""

__author__ = "730557892"

secret_word: str = ("python")

user_guess: str = input("What is your 6-letter guess? ")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

while len(user_guess) != len(secret_word):
    letters: int = len(secret_word)
    user_guess = input(f"That was not {letters} letters! Try again: ")
        
current_letter: int = 0
result: str = ""


while current_letter < len(secret_word):
    if secret_word[current_letter] == user_guess[current_letter]:
        result = result + GREEN_BOX 
    else:
        different_spot: bool = False 
        other_index: int = 0
        while different_spot is not True and other_index < len(secret_word):
            if secret_word[other_index] == user_guess[current_letter]:
                different_spot = True 
            else: 
                other_index = other_index + 1
            if different_spot is True:
                result = result + YELLOW_BOX
        if different_spot is False:
            result = result + WHITE_BOX
    current_letter = current_letter + 1

print(result)

if user_guess != secret_word:
    print("Not quite. Play again soon!")
else: 
    print("Woo! You got it!")