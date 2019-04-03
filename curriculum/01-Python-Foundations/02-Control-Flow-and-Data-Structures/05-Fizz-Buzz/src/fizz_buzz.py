#!/usr/bin/env python3
# TODO: Write a docstring
"""
fizz buzz poupipoupipoupipou
"""

def main():
    # TODO: implement the program using for loops
    numbers = range(1, 101)
    for number in numbers:
        if (number % 3 == 0):
            if (number % 5 == 0):
                print("Fizz Buzz")
            else:
                print("Fizz")
        else:
            if(number % 5 == 0):
                print("Buzz")
            else:
                print(number)


if __name__ == '__main__':
    main()
