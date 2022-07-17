import random


# Open file with list of sates
file = open("ListOfStates.txt").read().splitlines()


# Function draw random word from file_to_draw
def draw_random_country(file_to_draw):
    print("This is your word: ", end="")
    return random.choice(file_to_draw).upper()


# Function responsible for displaying country
def display_word(word_to_guess, letters):
    for char in word_to_guess:
        if char in letters:
            print(char, end="")
        elif char == " ":
            print(" ", end="")
        else:
            print("_", end="")
    print()


play_again = True
while play_again:
    array_letters = set()
    user_accept = False
    # Setting number of lives. Input is validate, user can choose only positive number of lives
    try:
        number_of_tries = int(input("How many lives do you want?: "))
        if number_of_tries <= 0:
            print("You need to choose positive value of lives. Try again")
    except ValueError:
        print("Invalid value. Try again")
        continue
    # Draw random country and display on the screen
    random_country = draw_random_country(file)
    display_word(random_country, array_letters)
    # While loop - responsible for changing country, if user want change it.
    while not user_accept:
        yes_or_no = input("Do you want change your country to guess (Yes or No)? : ").lower()
        if yes_or_no in ["yes", "y"]:
            random_country = draw_random_country(file)
            display_word(random_country,array_letters)
        elif yes_or_no in ["no", "n"]:
            user_accept = True
        else:
            print("Wrong choice. Try again.")
            continue
    # The main part of code responsible for the game
    while number_of_tries != 0:
        print("-" * 20)
        print("Yours word looks like: ", end="")
        display_word(random_country, array_letters)
        print()
        user_choice = input("Choose letter from range A-Z (size of letter doesn't matter): ").upper()
        # Condition - user introduce too long char
        if len(user_choice) != 1:
            print("You must choose only one letter. Try again: ")
            continue
        # Condition - user introduce another char - not letter
        if not user_choice.isalpha():
            print("Wrong choice, try one more time. Only expected format A-Z :)")
            continue
        # Condition - user use again the same letter
        if user_choice in array_letters:
            print("You choose this latter early, try again: ")
            continue
        array_letters.add(user_choice)
        # Condition - letter exist in country to guess
        if random_country.find(user_choice) == -1:
            number_of_tries -= 1
            print("Sorry your letter isn't in this word :( ")
            print("Your number of lives is %d " % number_of_tries)
            continue
        # Condition - compare two word user and word to guess
        if set(random_country.replace(" ", "")).issubset(array_letters):
            print("You won! Congratulations! Your word is: %s" % random_country)
            number_of_tries = 0
    user_accept = False
    # Condition - play again ?
    if number_of_tries == 0:
        print("You lost all your lives. Your country was: " + random_country)
        while not user_accept:
            play_again_choice = input("You want play again (Yes or No)?: ").lower()
            if play_again_choice in ["yes", "y"]:
                break
            elif play_again_choice in ["no", "n"]:
                play_again = False
                break
            else:
                print("Wrong choice. Try again.")
                continue



