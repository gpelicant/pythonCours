#!/usr/bin/env python3
# TODO: Write a docstring
"""
A program which computes BMI
"""

def main():
    # TODO: input for name: name
    name = input("What's your name? ").capitalize()
    # TODO: input for height in centimeters: height
    height = int(input("How tall are you (in cm)? "))
    # TODO: input for weight: weight
    weight = int(input("How much do you weight (in kg)? "))
    # TODO: compute the BMI: bmi
    bmi = weight / (height / 100)**2
    # TODO: print a greeting to the user followed by it's BMI
    # Example: "Hello Georges, your BMI is 26.75!"
    print('Hello {}, your BMI is {:.2f}!'.format(name, bmi))


if __name__ == '__main__':
    main()
