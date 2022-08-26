"""EXO1 - Chardle - A cute step toward Wordle."""

__author__ = "730557892"

five_character_word: str = input("Enter a 5-character word: ")

if len(five_character_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()

single_character: str = input("Enter a single character: ") 

if len(single_character) != 1:
    print("Error: Character must be a single character.")
    exit()

print("Searching for " + single_character + " in " + five_character_word)

matching_characters = 0

FIRSTCHARACTER: str = five_character_word[0]

if single_character == FIRSTCHARACTER:
    print(single_character + " found at index 0")
    matching_characters = matching_characters + 1

SECONDCHARACTER: str = five_character_word[1]

if single_character == SECONDCHARACTER:
    print(single_character + " found at index 1")
    matching_characters = matching_characters + 1

THIRDCHARACTER: str = five_character_word[2]

if single_character == THIRDCHARACTER:
    print(single_character + " found at index 2")
    matching_characters = matching_characters + 1

FOURTHCHARACTER: str = five_character_word[3]

if single_character == FOURTHCHARACTER:
    print(single_character + " found at index 3")
    matching_characters = matching_characters + 1
   
FIFTHCHARACTER: str = five_character_word[4]

if single_character == FIFTHCHARACTER:
    print(single_character + " found at index 4")
    matching_characters = matching_characters + 1
    

if matching_characters == 0:
    print("No instances of " + single_character + " found in " + five_character_word)

if matching_characters == 1:
    print("1 instance of " + single_character + " found in " + five_character_word)

if matching_characters > 1: 
    print(str(matching_characters) + " instances of " + single_character + " found in " + five_character_word)
