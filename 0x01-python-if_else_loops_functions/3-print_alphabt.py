#!/usr/bin/python3

"""Print lowercase alphabet, except 'q' and 'e'"""
for letter in range(97, 123):
    if chr(letter) in ('e', 'q'):
        continue
    print("{}".format(chr(letter)), end="")
