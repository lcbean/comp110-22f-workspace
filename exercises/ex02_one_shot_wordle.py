"""EX02 - One-Shot Wordle."""

__author__ = "730557892"

# picking a secret word (python in this case) and asking the user to guess a word with the same amount of letters

secret_word: str = ("python")
letters: int = len(secret_word)
user_guess: str = input(f"What is your {letters}-letter guess? ")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

# while loop checks to see if the player's guess is the same amount of letters as the secret word and if not asks them to guess again 
# until they pick a word with the right amount of letters

while len(user_guess) != len(secret_word):
    user_guess = input(f"That was not {letters} letters! Try again: ")
        

# checks each letter in the guessed word for matching letters in the secret word
# if the letter is the same at the same index on each word a green box is added, if not, a while loop checks if the current letter
# being checked in the user's guess is at another index in the secret word, if this is true, a yellow box is added and if not
# a white box is added. The next letter is then checked for a match as the loop resets

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

# the player wins if they guess the word right and lose if they're wrong

if user_guess != secret_word:
    print("Not quite. Play again soon!")
else: 
    print("Woo! You got it!")