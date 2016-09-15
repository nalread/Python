prompt = ("> ")
my_list = []
action = None
name = input("Hello user. What is your name?\n" + prompt)

def print_em_all():
    print ("Here are currently listed items:")
    for item in my_list:
        print(item)

def show_help():
    print ("""Here's an available list of commands:
    SHOW - shows current contents of the list;
    DONE - shows current contents of the list and terminates the program;
    HELP - directs you to this screen""")

print("It's nice to meet you, {}. What would you like to add to your \
list?\n(Type HELP for list of commands)".format(name))

while True:
    action = input(prompt)
    if action == "SHOW":
        print_em_all()
    elif action == "HELP":
        show_help()
    elif action == "DONE":
        break
    else:
        my_list.append(action)

print_em_all()
