#!/usr/bin/python3
# 12-fizzbuzz.py

def fizzbuzz():
    """FizzBuzz!"""

    for i in range(1, 101):
        if i == 100:
            print("Buzz", end=" ")
        elif i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print("{}".format(i), end=" ")
