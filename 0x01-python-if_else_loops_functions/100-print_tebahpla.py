#!/usr/bin/python3

""""Print the alphabet in reverse order alternating upper- and lower-case."""
for c in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(c - ((c % 2) * 32))), end="")
