input_list = []
total_sum = 0

for i in range(5):
    cur_input = int(raw_input("Enter a number: "))
    input_list.append(cur_input)

for i in input_list:
    total_sum += i

print "The total is {}".format(total_sum)