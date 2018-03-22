# -*- coding: utf-8 -*-

"""

filename: coding training ex 46
date: 2018-03-22
purpose: count word frequency

"""


def main():
    target_file_name = raw_input("Enter target file name: ")

    with open(target_file_name, "r") as f:
        file_content = f.read()

    word_set = list(set(file_content.split()))

    word_cnt_dict = {}

    for i in word_set:
        word_cnt_dict[i] = file_content.count(i)

    result_list = sorted(word_cnt_dict, key=lambda k: word_cnt_dict[k])[::-1]

    for i in result_list:
        print "%-10s : " % i + "*" * word_cnt_dict[i]
    return


if __name__ == "__main__":
    main()
