def get_input_name(file_name):
    with open(file_name, "w") as f:
        while True:
            cur_name = raw_input("Enter name list: ")
            if cur_name == "":
                break
            else:
                f.write(cur_name + "\n")

def print_result(file_name):
    with open(file_name, "r") as f:
        name_list = f.readlines()
        print "\nTotal of {} names".format(len(name_list))
        print "-----------------\n"
        for i in name_list:
            print i.replace("\n", "")

def main():
    get_input_name("name_list")
    print_result("name_list")
    return

if __name__ == "__main__":
    main()