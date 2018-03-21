ord_amount = float(raw_input("What is the order amount? "))
state = raw_input("What is the state? ")

tax_rate = 0.055

if str(state) == "WI":
    print "The subtotal is {}".format(ord_amount)
    tax = tax_rate * ord_amount
    print "The tax is {}".format(tax)
    total = ord_amount + tax
    print "The total os {}".format(total)

if str(state) != "WI":
    tax = tax_rate * ord_amount
    total = ord_amount + tax
    print "The total os {}".format(total)




