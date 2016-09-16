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
print (word)
# print as many underscores as there are letters in word
# take a guess
# loop: check every letter in word against guessed letter. If matches - uncover it by altering underscore with the letter
