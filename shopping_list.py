prompt = ("> ")
my_list = []
action = None
name = input("Hello user. What is your name?\n" + prompt)

print("It's nice to meet you, {}. What would you like to add to your \
list?\n(Input DONE to finish)".format(name))

while True:
    action = input(prompt)
    if action == "DONE":
        break
    else:
        my_list.append(action)
for item in my_list:
    print(item)
