import random

name_list = []

index = random.randrange(len(name_list))

print "The winner is... {}".format(name_list[index])

while True:
    cur_name = raw_input("Enter a name: ")
    if cur_name == "":
        break
    else:
        name_list.append(cur_name)