import random

word_list = [
'banana',
'mom',
'bang',
'bangity'
]
word = word_list[random.randint(0, len(word_list) - 1)]
word_shown = []
index = 0
for i in word:
    word_shown.append("_")

print (word_shown)

while True:
    guess = input("Guess a single letter\n>").lower()
    if len(guess) > 1:
        print ("Please enter just one letter at a time!")
    else:
        for j in word:
            if j == guess:
                word_shown[index] = guess
                index += 1
            else:
                index += 1

        print (word_shown)
        index = 0
        if "_" not in word_shown:
            break
print ("Grats, you won!")
