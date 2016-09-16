import random

number = random.randint(1, 10)

while True:
    print ("I'm thinking about a number between 1 and 10. What's your guess?")
    try:
        guess = int(input("> "))
    except ValueError:
        print ("That's not a valid number!")
    else:
        if guess > number:
            print ("Too high")
        elif guess < number:
            print ("Too low")
        else:
            break

print ("Grats, you won!")
