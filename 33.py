# -*- coding: utf-8 -*-

"""

filename:???
date:
purpose:

"""
import random


def main():
    answer_list = ["Yes", "No", "Maybe", "Ask again later"]
    raw_input("What is your question? ")
    cur_index = random.randrange(0, 4)

    print answer_list[cur_index]
    
    return


if __name__ == "__main__":
    main()


