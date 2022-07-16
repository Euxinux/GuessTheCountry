import random
# Open file with list of sates and draw one of them
file = open("ListOfStates.txt").read().splitlines()
random_word = random.choice(file).upper()
# Set the number of lives
number_of_tries = 100
array_letter = set()

# Function responsible for displaying word
def display_word(word_to_guess, array_letter):
    for char in word_to_guess:
        if char in array_letter:
            print(char, end="")
        elif char == " ":
            print(" ", end="")
        else:
            print("_",end="")
    print()
while number_of_tries != 0:
    print("-" * 20)
    print("Yours word looks like: ", end="")
    display_word(random_word,array_letter)
    user_choice = input("Choose letter from range A-Z (size of letter doesn't matter): ").upper()
    if len(user_choice) != 1:
        print("You must choose only one letter. Try again: ")
        continue
    if not user_choice.isalpha():
        print("Wrong choice, try one more time. Only expected format A-Z :)")
        continue
    if user_choice in array_letter:
        print("You choose this latter early, try again: ")
        continue
    array_letter.add(user_choice)
    if random_word.find(user_choice) == -1:
        number_of_tries -= 1
        print("Sorry your letter isn't in this word :( ")
        print("Your number of lives is %d " % number_of_tries)
        continue

    if set(random_word.replace(" ", "")).issubset(array_letter):
        print("You won! Congratulations! Your word is: %s" % random_word)
        break
