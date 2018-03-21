import re

def check_ID(emp_ID):
    filter = re.compile("[A-Z]{2}-[0-9]{4}")
    m = filter.match(emp_ID)
    if m:
        return True
    else:
        print "{} is not a valid ID".format(emp_ID)
        return False

def check_first_name(first_name):
    if first_name == "":
        print "The first name must be filed in"
        return False

    if len(first_name) < 2:
        print "{} is not a valid first name. It is too short.".format(first_name)
        return False
    else:
        return True

def check_last_name(last_name):
    if last_name == "":
        print "The last name must be filed in"
        return False
    if len(last_name) < 2:
        print "{} is not a valid last name. It is too short.".format(last_name)
        return False
    else:
        return True

def check_ZIP_code(zip_code):
    filter = re.compile("[0-9]+")
    m = filter.match(zip_code)
    if m:
        return True
    else:
        print "The ZIP code must be numeric"
        return False

def validateInput(first_name, last_name, zip_code, emp_ID):
    bool_first = check_first_name(first_name)
    bool_last = check_last_name(last_name)
    bool_zip = check_ZIP_code(zip_code)
    bool_emp = check_ID(emp_ID)
    if bool_first & bool_last & bool_emp & bool_zip:
        print "There were no errors found"
        return True
    else:
        return False

first_name = str(raw_input("Enter the first name: "))
last_name = str(raw_input("Enter the last name: "))
zip_code = str(raw_input("Enter the ZIP code: "))
emp_ID = str(raw_input("Enter an employee ID: "))

bool_total = validateInput(first_name, last_name, zip_code, emp_ID)




