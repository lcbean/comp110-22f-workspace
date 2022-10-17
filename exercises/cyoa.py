"""Ex06 - Create Your Own Adventure."""

__author__ = "730557892"


HEART_EYES: str = "\U0001F970"
HEART_ARROW: str = "\U0001F498"
PINK_HEART: str = "\U0001F497"
TEAR: str = "\U0001F622"
CELEBRATE: str = "\U0001F973"

points: int = 0
player: str = ""
initial_choice: str = ""


def greet() -> None:
    """Welcomes the player and asks for their name."""
    print(f"Welcome to {HEART_ARROW}Celebrity Bachelorette{HEART_ARROW}, the game where three dashing celebrity heart throbs compete for the affections of one lucky lady or lad: {HEART_EYES}YOU!{HEART_EYES} ")
    global player
    player = input("But first, what is your name? ")


def beginning_choice_input() -> None:
    """Indicates which of the four choices the player chooses."""
    global initial_choice
    initial_choice = input("Please enter 1, 2, 3, or 4 to lock in your decision. ")


def compatability() -> None:
    """Player can choose one of the three men and start playing the compatability game for their choice."""
    print(f"Welcome to the Compatability Test, {player}!")
    meet_the_men: str = input("Are you ready to meet the men!?! [1] Yes, please! [2] No, I've already met them. ")
    if meet_the_men == "1":
        print("Without further ado, the first of these three lucky men is...")
        print("Chris Evans!")
        print("Chris is an actor known for his role as Captain America in the Marvel Cinematic Universe. He can rock a sweater and loves his dog, Dodger! Give it up for Chris!")
        print("The next certified hottie on our list is...")
        print("Robert Pattinson!")
        print("Robert first shot into fame after his iconic role as the vampire Edward Cullen in the Twilight series but has since made a name for himself in Hollywood as a more serious actor in critically acclaimed films from The Light House to The Batman. He can appear a little reserved, but he's just a big ol softie who wants love just like everyone else.")
        print("And last but not least...")
        print("Miles Teller!")
        print("Miles is an actor (I'm sensing a pattern here) who recently gained traction for the major summer blockbuster Top Gun: Maverick. Who can resist that stache?")
        # player gains 5 love points for meeting the men 
        global points
        points += 5
    print("Now that you know the men, who would you like to test first?")
    test_choice: str = input("[1] Chris Evans [2] Robert Pattinson [3] Miles Teller ")
    if test_choice == "1":
        chris_test()
    if test_choice == "2":
        robert_test()
    if test_choice == "3":
        miles_test()

    
def chris_test() -> None:
    """Performs compatability test with Chris Evans."""
    print("The Compatability Test asks you 10 questions concerning various topics associated with successful relationships. Depending on how your answers compare to Chris's, you have the chance to gain Love Points for each question. Just type the letter of the answer choice to lock it in. Good luck!")
    test_points: int = 0
    global points
    question_1: str = input("1. Would you consider yourself more of an extrovert or an introvert?\n [A] Extrovert\n [B] Introvert\n")
    if question_1 == "B":
        test_points += 5
    question_2: str = input("2. Would you consider yourself a gym rat?\n [A] Yes\n [B] No\n")
    if question_2 == "A":
        test_points += 5
    question_3: str = input("3. What is your astrological sign?\n [A] Aries\n [B] Taurus\n [C] Gemini\n [D] Cancer\n [E] Leo\n [F] Virgo\n [G] Libra\n [H] Scorpio\n [I] Sagittarius\n [J] Capricorn\n [K] Aquarius\n [L] Pisces\n")
    if question_3 == "A" or "G" or "K":
        test_points += 5
    if question_3 == "B" or "D" or "H":
        # least compatible star signs deducts points
        test_points -= 5
    question_4: str = input("4. What music do you listen to?\n [A] Classic rock\n [B] Pop\n [C] Indie\n [D] Country\n [E] Rap\n")
    if question_4 == "A":
        test_points += 5
    question_5: str = input("5. Which of the following movies would you rather watch?\n [A] Harry Potter and the Goblet of Fire\n [B] Whiplash\n [C] Knives Out\n [D] Divergent\n")
    if question_5 == "C":
        test_points += 5
    question_6: str = input("6. Which of the following foods would you be most likely to eat?\n [A] Cheeseburger\n [B] Pesto eggs\n [C] Spicy tuna roll\n [D] Chimichurri steak\n")
    if question_6 == "B":
        test_points += 5
    question_7: str = input("7. What is your ideal date?\n [A] A walk through the park with your dogs\n [B] Coffee then hitting up a bookstore\n [C] Homemade candlelit dinner\n [D] Strawberry picking\n")
    if question_7 == "A":
        test_points += 5
    question_8: str = input("8. Which city would you rather live in?\n [A] NYC\n [B] San Francisco\n [C] Boston\n [D] LA\n")
    if question_8 == "C":
        test_points += 5
    question_9: str = input("9. Which of these hobbies are you interested in most?\n [A] Tap dancing\n [B] Cooking\n [C] Reading\n [D] Hiking\n")
    if question_9 == "A":
        test_points += 5
    question_10: str = input("10. What is your favorite season?\n [A] Summer\n [B] Fall\n [C] Winter\n [D] Spring\n")
    if question_10 == "C":
        test_points += 5
    # if they get less than 7 questions right 
    if test_points < 35:
        print(f"It looks like you and Chris aren't compatible. Better luck next time!\n {PINK_HEART}{PINK_HEART}{PINK_HEART} Total Love Points: {points} {PINK_HEART}{PINK_HEART}{PINK_HEART}")
    else: 
        # adds the points earned from the test to the total love points
        points += test_points
        print(f"You and Chris are a perfect match!{CELEBRATE} You have gained {test_points} love points as your prize!\n {PINK_HEART}{PINK_HEART}{PINK_HEART} Total Love Points: {points} {PINK_HEART}{PINK_HEART}{PINK_HEART}")


def robert_test() -> None:
    """Performs compatability test for Robert Pattinson."""
    print("The Compatability Test asks you 10 questions concerning various topics associated with successful relationships. Depending on how your answers compare to Chris's, you have the chance to gain Love Points for each question. Just type the letter of the answer choice to lock it in. Good luck!")
    test_points: int = 0
    global points
    question_1: str = input("1. Which of the following hobbies interests you?\n [A] Jogging\n [B] Playing the guitar\n [C] Watching football\n [D] Thrifting\n")
    if question_1 == "B":
        test_points += 5
    question_2: str = input("2. What music do you listen to?\n [A] Rap\n [B] Pop\n [C] Blues\n [D] Indie/alternative\n")
    if question_2 == "C":
        test_points += 5
    question_3: str = input("3. Which of the following movies do you prefer?\n [A] The Spectacular Now\n [B] The Nanny Diaries\n [C] The Hunger Games\n [D] Good Time\n")
    if question_3 == "D":
        test_points += 5
    question_4: str = input("4. Which city would you rather live in?\n [A] LA\n [B] NYC\n [C] Atlanta\n [D] Philly\n")
    if question_4 == "A":
        test_points += 5
    question_5: str = input("5. Would you consider yourself more of an extrovert or introver?\n [A] Extrovert\n [B] Introvert\n")
    if question_5 == "B":
        test_points += 5
    question_6: str = input("6. Which of the following foods would you eat?\n [A] Sushi\n [B] Dino nuggets\n [C] Chicken parm\n [D] BLT\n")
    if question_6 == "B":
        test_points += 5
    question_7: str = input("7. What is your favorite season?\n [A] Fall\n [B] Winter\n [C] Spring\n [D] Summer\n")
    if question_7 == "A":
        test_points += 5
    question_8: str = input("8. What is your ideal date?\n [A] Picnic in the park\n [B] Twilight marathon\n [C] Rock climbing\n [D] Pottery painting\n")
    if question_8 == "D":
        test_points += 5
    question_9: str = input("9. Which of these qualities is most important for you in a partner?\n [A] Good sense of humor\n [B] Good looking\n [C] Work ethic\n [D] Intelligent\n")
    if question_9 == "A":
        test_points += 5
    question_10: str = input("10. What is your astrological sign?\n [A] Aries\n [B] Taurus\n [C] Gemini\n [D] Cancer\n [E] Leo\n [F] Virgo\n [G] Libra\n [H] Scorpio\n [I] Sagittarius\n [J] Capricorn\n [K] Aquarius\n [L] Pisces\n")
    if question_10 == "B" or "H" or "L" or "J":
        test_points += 5
    if question_10 == "A" or "I" or "C":
        test_points -= 5
    if test_points < 35:
        print(f"It looks like you and Robert aren't compatible. Better luck next time!\n *** Total Love Points: {points} *** ")
    else:
        points += test_points
        print(f"You and Robert are a perfect match!{CELEBRATE} You have gained {test_points} love points as your prize!\n {PINK_HEART}{PINK_HEART}{PINK_HEART} Total Love Points: {points} {PINK_HEART}{PINK_HEART}{PINK_HEART}")


def miles_test() -> None:
    """Performs compatability test with Miles Teller."""
    print("The Compatability Test asks you 10 questions concerning various topics associated with successful relationships. Depending on how your answers compare to Chris's, you have the chance to gain Love Points for each question. Just type the letter of the answer choice to lock it in. Good luck!")
    test_points: int = 0
    global points
    question_1: str = input("1. Would you consider yourself more of an extrovert or an introvert?\n [A] Extrovert\n [B] Introvert\n")
    if question_1 == "A":
        test_points += 5
    question_2: str = input("2. Would you consider yourself a gym rat?\n [A] Yes\n [B] No\n")
    if question_2 == "A":
        test_points += 5
    question_3: str = input("3. What is your astrological sign?\n [A] Aries\n [B] Taurus\n [C] Gemini\n [D] Cancer\n [E] Leo\n [F] Virgo\n [G] Libra\n [H] Scorpio\n [I] Sagittarius\n [J] Capricorn\n [K] Aquarius\n [L] Pisces\n")
    if question_3 == "D" or "H" or "L":
        test_points += 5
    if question_3 == "A" or "E" or "I":
        # least compatible star signs deducts points
        test_points -= 5
    question_4: str = input("4. What music do you listen to?\n [A] Rock\n [B] Pop\n [C] Indie\n [D] Country\n [E] Rap\n")
    if question_4 == "A" or "E":
        test_points += 5
    question_5: str = input("5. Which of the following movies would you rather watch?\n [A] Minions\n [B] Whiplash\n [C] Scream\n [D] The Truman Show\n")
    if question_5 == "B":
        test_points += 5
    question_6: str = input("6. Which of the following foods would you be most likely to eat?\n [A] Steak\n [B] Burrito bowl\n [C] Pizza\n [D] Meatloaf\n")
    if question_6 == "A":
        test_points += 5
    question_7: str = input("7. What is your ideal date?\n [A] A walk through the park with your dogs\n [B] Coffee then hitting up a bookstore\n [C] Homemade candlelit dinner\n [D] Trip to Bali\n")
    if question_7 == "D":
        test_points += 5
    question_8: str = input("8. Which city would you rather live in?\n [A] NYC\n [B] San Francisco\n [C] Boston\n [D] LA\n")
    if question_8 == "D":
        test_points += 5
    question_9: str = input("9. Which of these hobbies are you interested in most?\n [A] Boxing\n [B] Reading\n [C] Golfing\n [D] Traveling\n")
    if question_9 == "C":
        test_points += 5
    question_10: str = input("10. What is your favorite season?\n [A] Summer\n [B] Fall\n [C] Winter\n [D] Spring\n")
    if question_10 == "A":
        test_points += 5
    # if they get less than 7 questions right 
    if test_points < 35:
        print(f"It looks like you and Miles aren't compatible. Better luck next time!\n *** Total Love Points: {points} ***")
    else: 
        # adds the points earned from the test to the total love points
        points += test_points
        print(f"You and Miles are a perfect match!{CELEBRATE} You have gained {test_points} love points as your prize!\n {PINK_HEART}{PINK_HEART}{PINK_HEART} Total Love Points: {points} {PINK_HEART}{PINK_HEART}{PINK_HEART}")


def trivia() -> None:
    """Starts a trivia game with a random man."""
    global points
    print(f"Welcome to trivia mode, {player}!\n In this game, a contestant will be randomly chosen for you, after which you will answer a series of trivia questions about them. This is another chance to earn those Love Points! Good luck!")
    to_continue: str = input("To continue, please type * ")
    if to_continue == "*":
        print("And the mystery contestant is...")
        from random import randint
        random_choice: int = randint(1, 3)
        if random_choice == 1:
            print("Chris Evans!")
            chris_trivia()
        if random_choice == 2:
            print("Robert Pattinson!")
            robert_trivia()
        if random_choice == 3:
            print("Miles Teller!")
            miles_trivia()


def chris_trivia() -> None:
    """Trivia game for Chris Evans."""
    print("Lets see how much you know about your potential dream man!")
    test_points: int = 0
    question_1: str = input("1. What was Chris's first big movie role?\n [A] The Nanny Diaries\n [B] Captain America\n [C] The Fantastic 4\n [D] Not Another Teen Movie\n")
    if question_1 == "D":
        test_points += 5
    question_2: str = input("2. What is Chris Evans's brothers name?\n [A] Scott\n [B] Mark\n [C] Steve\n [D] Vincent\n")
    if question_2 == "A":
        test_points += 5
    question_3: str = input("3. What was his nickname on the set of Captain America?\n [A] Chrissy\n [B] Dorito\n [C] Captain Little Ass\n")
    if question_3 == "C":
        test_points += 5
    question_4: str = input("4. True or False: He has been in more comic book movies than any other actor in Hollywood.\n [T]\n [F]\n")
    if question_4 == "T":
        test_points += 5
    question_5: str = input("5. What is his dads profession?\n [A] Actor\n [B] Dentist\n [C] Lawyer\n [D] Producer\n")
    if question_5 == "B":
        test_points += 5
    question_6: str = input("6. Who was his celebrity crush?\n [A] Julia Roberts\n [B] Scarlett Johansson\n [C] Sandra Bullock\n [D] Anne Hathaway\n")
    if question_6 == "C":
        test_points += 5
    question_7: str = input("7. What is his alma mater?\n [A] Lee Strasberg Theatre Institute\n [B] UNC\n [C] NYU\n [D] Julliard\n")
    if question_7 == "A":
        test_points += 5
    question_8: str = input("8. What was his first film?\n [A] Captain America\n [B] The Nanny Diaries\n [C] Not Another Teen Movie\n [D] The Newcomers\n")
    if question_8 == "D":
        test_points += 5
    question_9: str = input("9. True or False: Robert Downey Jr. was the one who convinced him to take the role of Captain America.\n [T]\n [F]\n")
    if question_9 == "T":
        test_points += 5
    question_10: str = input("10. What movie does he look best in?\n [A] Knives Out\n [B] Captain America\n [C] Infinity War\n [D] Snowpiercer\n")
    if question_10 == "A":
        test_points += 5
    if test_points < 35:
        print("Looks like you need to brush up on your Chris Evans facts. No Love Points for you! Better luck next time!")
    else: 
        global points
        points += test_points
        print(f"Wow, {player}, you really know your stuff!{CELEBRATE} Congratulations you've earned {test_points} Love Points!\n {PINK_HEART}{PINK_HEART}{PINK_HEART} Total Love Points: {points} {PINK_HEART}{PINK_HEART}{PINK_HEART}")


def robert_trivia() -> None:
    """Trivia game for Robert Pattinson."""
    print("Lets see how much you know about your potential dream man!")
    test_points: int = 0
    question_1: str = input("1. What instrument can he play?\n [A] Guitar\n [B] Violin\n [C] Cello\n [D] Flute\n")
    if question_1 == "A":
        test_points += 5
    question_2: str = input("2. Who was his celebrity idol?\n [A] Dick Van Dyke\n [B] Jack Nicholson\n [C] Robert De Niro\n [D] Morgan Freeman\n")
    if question_2 == "B":
        test_points += 5
    question_3: str = input("3. True or False: He beat 3,000 people for the role of Edward Cullen.\n [T]\n [F]\n")
    if question_3 == "T":
        test_points += 5
    question_4: str = input("4. True or False: He always wanted to be an actor.\n [T]\n [F]\n")
    if question_4 == "F":
        test_points += 5
    question_5: str = input("5. His role in what movie was written specifically for him?\n [A] The Batman\n [B] Good Time\n [C] Twilight\n [D] The Devil All the Time\n")
    if question_5 == "B":
        test_points += 5
    question_6: str = input("6. What singer was he in a relationship from 2014-2017?\n [A] Rihanna\n [B] Lorde\n [C] FKA Twigs\n [D] Kristen Stewart\n")
    if question_6 == "C":
        test_points += 5
    question_7: str = input("7. What is his favorite video game?\n [A] Minecraft\n [B] Fortnite\n [C] GTA V\n [D] Final Fantasy VII\n")
    if question_7 == "D":
        test_points += 5
    question_8: str = input("8. True or False: He has two brothers.\n [T]\n [F]\n")
    if question_8 == "F":
        test_points += 5
    question_9: str = input("9. What skill did he learn for Harry Potter and the Goblet of Fire?\n [A] Horseback riding\n [B] Scuba diving\n [C] Tae Kwon Do\n")
    if question_9 == "B":
        test_points += 5
    question_10: str = input("10. What age was he in Harry Potter?\n [A] 22\n [B] 21\n [C] 17\n [D] 30\n")
    if question_10 == "C":
        test_points += 5
    if test_points < 35:
        print("Looks like you need to brush up on your Robert Pattinson facts. No Love Points for you! Better luck next time!")
    else:
        global points
        points += test_points 
        print(f"Wow, {player}, you really know your stuff!{CELEBRATE} Congratulations you've earned {test_points} Love Points!\n {PINK_HEART}{PINK_HEART}{PINK_HEART} Total Love Points: {points} {PINK_HEART}{PINK_HEART}{PINK_HEART}")


def miles_trivia() -> None:
    """Trivia game for Miles Teller."""
    print("Lets see how much you know about your potential dream man!")
    test_points: int = 0
    question_1: str = input("1. What actress did he star in The Spectacular Now and Divergent with?\n [A] Florence Pugh\n [B] Gal Gadot\n [C] Shailene Woodley\n [D] Emma Watson\n")
    if question_1 == "C":
        test_points += 5
    question_2: str = input("2. What is his alma mater?\n [A] NYU\n [B] Julliard\n [C] UCLA\n [D] USC\n")
    if question_2 == "A":
        test_points += 5
    question_3: str = input("3. True or False: He played the same character in the stage musical Footloose that he did in the movie version.\n [T]\n [F]\n")
    if question_3 == "T":
        test_points += 5
    question_4: str = input("4. True or False: The scars on his face are from a car accident.\n [T]\n [F]\n")
    if question_4 == "T":
        test_points += 5
    question_5: str = input("5. He starred in what two movies with Michael B. Jordan?\n [A] That Awkward Moment and Fantastic Four\n [B] Whiplash and Divergent\n [C] The Hunger Games and Twilight\n")
    if question_5 == "A":
        test_points += 5
    question_6: str = input("6. What was his first feature film?\n [A] Whiplash\n [B] The Spectacular Now\n [C] Rabbit Hole\n [D] Divergent\n")
    if question_6 == "C":
        test_points += 5
    question_7: str = input("7. What is his dad's profession?\n [A] Nuclear power\n [B] Dentist\n [C] Lawyer\n [D] Doctor\n")
    if question_7 == "A":
        test_points += 5
    question_8: str = input("8. True or False: He can actually play the drums.\n [T]\n [F]\n")
    if question_8 == "T":
        test_points += 5
    question_9: str = input("9. What sport did he play growing up?\n [A] Soccer\n [B] Baseball\n [C] Baskbetbal\n [D] Tennis\n")
    if question_9 == "B":
        test_points += 5
    question_10: str = input("10. What's the name of the restaurant he worked at in high school?\n [A] Chilis\n [B] Olive Garden\n [C] Wendys\n [D] Crackers\n")
    if question_10 == "D":
        test_points += 5
    if test_points < 35:
        print("Looks like you need to brush up on your Miles Teller facts. No Love Points for you! Better luck next time!")
    else: 
        global points
        points += test_points
        print(f"Wow, {player}, you really know your stuff!{CELEBRATE} Congratulations you've earned {test_points} Love Points!\n {PINK_HEART}{PINK_HEART}{PINK_HEART} Total Love Points: {points} {PINK_HEART}{PINK_HEART}{PINK_HEART}")


def cash_in(points: int) -> int:
    """The player can spend their points for the chance to win a date with a man of their choice."""
    print(f"Welcome to the Love Exchange, {player}!\n In this mode, you have the chance to cash in your points for the chance to win a date with one of the men.")
    spend_points: str = input("First, indicate which man you would like to try for:\n [1] Chris Evans\n [2] Robert Pattinson\n [3] Miles Teller\n")
    choice_man: str = ""
    if spend_points == "1":
        choice_man = "Chris Evans"
    if spend_points == "2":
        choice_man == "Robert Pattinson"
    if spend_points == "3":
        choice_man == "Miles Teller"
    to_continue: str = input(f"Great choice, {player}! It costs 20 Love Points to spin the wheel of love. Whenever you're ready, please type * ")
    if to_continue == "*":
        from random import randint
        success: int = 1
        wheel_spin: int = randint(1, 3)
        if success == wheel_spin:
            print(f"Congratulations, {player}, you won a date with {choice_man}!{CELEBRATE} Thanks for playing Celebrity Bachelorette!\n *** Total Love Points: {points}")
            quit()
        else:
            print(f"No dice! Better luck next time.{TEAR}")
            points -= 20
    return points 


def main() -> None:
    """Entrypoint of the game."""
    global points
    points = 0
    greet()
    while initial_choice != "4":
        print(f"Hi, {player}! Would you like to:\n [1] Test your compatability with a celebrity hottie of your choice\n [2] Play the trivia game of love\n [3] Cash in those Love Points for the chance of winning a date with your dream man\n [4] Give up on love entirely\n")
        beginning_choice_input()
        if initial_choice == "1":
            compatability()
        if initial_choice == "2":
            trivia()
        if initial_choice == "3":
            if points > 20:
                points = cash_in(points)
                print(f"{PINK_HEART}{PINK_HEART}{PINK_HEART} Total Love Points: {points} {PINK_HEART}{PINK_HEART}{PINK_HEART}")
            else:
                print("You don't have enough Love Points for this experience. Try again later.")
        if initial_choice == "4":
            print(f"So sorry to see you go!{TEAR} Try again soon!")
            print(f"{PINK_HEART}{PINK_HEART}{PINK_HEART} Total Love Points: {points} {PINK_HEART}{PINK_HEART}{PINK_HEART}")
            quit()
        

if __name__ == "__main__":
    main()