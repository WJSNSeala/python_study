# -*- coding: utf-8 -*-

"""

filename: coding training ex 45
date: 2018-03-22
purpose: specific word search

"""


def count_specific_word(target_file, old_word, new_word):
    with open(target_file, "r") as f:
        file_content = f.read()

    word_cnt = file_content.count(old_word)
    file_content = file_content.replace(old_word, new_word)

    return word_cnt, file_content


def main():
    target_file_name = raw_input("Enter target filename: ")
    result_tuple = count_specific_word(target_file_name, "utilize", "use")

    print "utilize: {}".format(result_tuple[0])

    modified_file_name = raw_input("Enter new filename: ")
    with open(modified_file_name, "w") as f:
        f.write(result_tuple[1])

    return


if __name__ == "__main__":
    main()
