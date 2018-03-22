# -*- coding: utf-8 -*-

"""

filename: coding training ex 44
date: 2018-03-22
purpose: parsing json data form

Improvement : find another way that doesn't use eval function

"""


def main():

    with open("products.json", "r") as f:
        input_data = eval(f.read())
        products_list = input_data['products']

    while True:
        bool_product = False
        product_name = raw_input("What is the product name? ")

        if product_name == "":
            return

        for i in products_list:

            if i['name'] == product_name:
                print "Name: {}".format(i['name'])
                print "Price: {}".format(i['price'])
                print "Quantity: {}".format((i['quantity']))
                bool_product = True
                break

        if bool_product:
            pass
        else:
            print "Sorry, that product was not found in our inventory."

    return


if __name__ == "__main__":
    main()
