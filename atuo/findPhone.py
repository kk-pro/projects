#!/usr/bin/python3

# usage : python3 findPhone.py "text file path"
# example : python3 findPhone.py 1.txt
import re, sys

filename = sys.argv[1]
def findn(filename):
    phonenum= re.compile(r'05\d\d\d\d\d\d\d\d')
    with open(filename) as f:
        for line in f:
            phone_number = re.search(phonenum, line)
            if phone_number:

                print("phone number found: "+phone_number.group())
            else:
                None
        print('done')


findn(filename)
