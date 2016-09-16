import random

# create wordlist
word_list = [
'banana',
'mom',
'bang',
'bangity'
]
# choose random word from wordlist
word = word_list[random.randint(0, len(word_list) - 1)]
word_shown = []
index = 0
guesses = 0
# create a list with word_shown with underscores
for i in word:
    word_shown.append("_")

print (word_shown)

# loop: check every letter in word against guessed letter. If matches - uncover
while guesses < 3:
    # take a guess
    guess = input("Guess a single letter\n>").lower()
    for j in word:
        if j == guess:
            word_shown[index] = guess
            index += 1
        else:
            # guesses += 1
            index += 1

    print (word_shown)
    index = 0
# it by altering underscore with the letter
