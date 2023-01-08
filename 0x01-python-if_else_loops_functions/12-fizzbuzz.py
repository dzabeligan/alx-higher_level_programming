#!/usr/bin/python3
"""
ALX Task 11
"""


def fizzbuzz():
    """fizzbuzz:
    Print Fizz for multiples of 3
    Print Buzz for multiples of 5
    Print FizzBuzz for multiples of 15
    Print number if the above conditions are not met
    """
    for num in range(1, 101):
        if num % 3 == 0:
            print("Fizz", end="")
        if num % 5 == 0:
            print("Buzz", end="")
        if num % 3 and num % 5:
            print(f"{num}", end="")
        print(" ", end="")
