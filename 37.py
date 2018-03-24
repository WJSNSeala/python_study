import random


def get_random_str(num, char_set):
    rand_str = ""
    while num > 0:
        rand_str += char_set[random.randrange(len(char_set))]
        num -= 1
    return rand_str


alpha_list = list("abcdefghijklmnopqrstuvwxyz")
numeric_list = list("0123456789")
special_list = list("~!@#$%^&*()?/><")

minimum_length = int(raw_input("What's the minumun length? "))
num_special = int(raw_input("How many special characters? "))
num_numeric = int(raw_input("How many number? "))

num_str = ""
spec_str = ""
alpha_str = ""

num_str = get_random_str(num_numeric, numeric_list)
spec_str = get_random_str(num_special, special_list)

max_length = random.randrange(minimum_length, minimum_length + 10)

alpha_str = get_random_str(max_length - num_special - num_numeric, alpha_list)

result = list(alpha_str)

for i in num_str:
    result.insert(random.randrange(len(result)), i)

for i in spec_str:
    result.insert(random.randrange(len(result)), i)

result_string = ""

for i in result:
    result_string += str(i)

print result_string

