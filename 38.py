def filter_Even_Numbers(org_list):
    new_list = []
    for i in org_list:
        if int(i) % 2 == 0:
            new_list.append(int(i))
    return new_list


def main():
    input_list = raw_input("Enter a list of numbers, separated by spaces: ").split()
    filter_list = filter_Even_Numbers(input_list)
    print filter_list

    return


if __name__ == "__main__":
    main()
