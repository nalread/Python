prompt = ("> ")
my_list = []
action = None
name = input("Hello user. What is your name?\n" + prompt)

print("It's nice to meet you, {}. What would you like to add to your \
list? (Input DONE to finish.)".format(name))

while action != "DONE":
    action = input(prompt)
    if action == "DONE":
        break
    else:
        my_list.append(action)
print(my_list)
