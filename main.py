#!/usr/bin/env python3

"""
Module defines logic to test number input and runs the game FizzBuzz up to 100 numbers.
"""

def check_fizzbuzz(number):
    """
    Takes a number as input and determines if it is divisible by 3 (fizz) or 5 (buzz)
    using the MODULUS (%) operator. Returns the appropriate response based on the check.
    """

    fizz = 3
    buzz = 5

    if (number%fizz == 0) & (number%buzz == 0):
        print("FizzBuzz")
    elif number%fizz == 0:
        print("Fizz")
    elif number%buzz == 0:
        print("Buzz")
    else:
        print(number)

if __name__ == '__main__':
    for i in range(0,101):
        check_fizzbuzz(i)
