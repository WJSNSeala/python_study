import random

alpha_list = list("abcdefghijklmnopqrstuvwxyz")
numeric_list = list("0123456789")
special_list = list("~!@#$%^&*()?/><")

minumum_length = int(raw_input("What's the minumun length? "))
num_special = int(raw_input("How many special characters? "))
num_numeric = int(raw_input("How many number? "))

num_str = ""
spec_str = ""
alpha_str = ""

for i in range(num_numeric):
    num_str += numeric_list[random.randrange(len(numeric_list))]

for i in range(num_special):
    spec_str += special_list[random.randrange(len(special_list))]

max_leng = random.randrange(minumum_length, minumum_length + 10)

for i in range(max_leng - num_special - num_numeric):
    alpha_str += alpha_list[random.randrange(len(alpha_list))]

print num_str
print spec_str
print alpha_str

result = list(alpha_str)

for i in num_str:
    result.insert(random.randrange(len(result)), i)

for i in spec_str:
    result.insert(random.randrange(len(result)), i)

result_string = ""

for i in result:
    result_string += str(i)

print result_string

