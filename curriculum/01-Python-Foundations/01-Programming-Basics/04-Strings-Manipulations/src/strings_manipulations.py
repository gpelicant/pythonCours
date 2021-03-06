#!/usr/bin/env python3
"""
A simple program to play with strings
"""


def main():

    ## Part 1: using string methods, print out what you're being asked
    # TODO: print the lowercase version of this string
    up_string = "A string with UPPERCASE"
    toto = up_string.lower()
    print(toto)

    # TODO: print the length of this string
    long_string = "A very very long string, don't you think?"
    titi = len(long_string)
    print(titi)

    ## Part 2
    username = "Kinari"
    timestamp = "04:50"
    url = "http://petshop.com/pets/mammals/cats"

    # TODO: print a log message using the variables above.
    # The message should have the same format as this one:
    # "Yogesh accessed the site http://petshop.com/pets/reptiles/pythons at 16:20."
    print(f"{username} accessed the site {url} at {timestamp}.")

    ## Part 3
    maria_string = "Maria loves {} and {}."
    # TODO: print out "Maria loves math and statistics." using .format()
    print(maria_string.format("math", "statistics"))


if __name__ == '__main__':
    main()
