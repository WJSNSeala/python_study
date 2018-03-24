# -*- coding: utf-8 -*-

"""

filename: ex 52 client
date: 2018-03-24
purpose: use requests module

"""
import requests


def main():
    target_url = "http://127.0.0.1:5000/application/json"
    r = requests.get(target_url)
    result_dict = eval(r.text)

    print "The current time is {}".format(result_dict["curtime"])


if __name__ == "__main__":
    main()
