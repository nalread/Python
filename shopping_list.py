prompt = ("> ")
my_list = []
action = None
# run = True
name = input("Hello user. What is your name?\n" + prompt)

print("It's nice to meet you, {}. What would you like to add to your \
list? (Input DONE to finish.)".format(name))

# while run == True:
while True:
    action = input(prompt)
    if action == "DONE":
        break
    # run = False
    else:
        my_list.append(action)
print(my_list)
