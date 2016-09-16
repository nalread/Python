import random

number = random.randint(1, 10)

def play_the_game():
    guesses = 0
    print ("I'm thinking about a number between 1 and 10. What's your guess?")
    while guesses < 5:
        try:
            guess = int(input("> "))
        except ValueError:
            print ("That's not a valid number!")
        else:
            if guess > number:
                print ("Too high")
                guesses += 1
            elif guess < number:
                print ("Too low")
                guesses += 1
            else:
                break

    if guesses < 5:
        print ("Grats, you won!")
    else:
        print ("Boo, you lost! My number was {}!".format(number))

play_the_game()

while True:
    print ("Do you want to play again?")
    answer = input("(Y)es or (N)o\n>").lower()
    if answer == 'y':
        play_the_game()
    elif answer == 'n':
        input("Bye!")
        quit()
