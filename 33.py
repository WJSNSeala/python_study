import random

answer_list = ["Yes", "No", "Maybe", "Ask again later"]

question = raw_input("What is your question? ")

cur_index = random.randrange(0, 4)

print answer_list[cur_index]

