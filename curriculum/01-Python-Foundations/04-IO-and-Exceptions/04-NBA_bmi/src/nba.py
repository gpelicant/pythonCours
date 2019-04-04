"""
NBA players
"""
import csv
from os import path


# TODO: implement `extract_height`


# TODO: implement `extract_height`


# TODO: implement `extract_height`


def main():
    weights, heights = load_data()
    bmis = [round(bmi(w, h), 2) for w, h in zip(weights, heights)]
    print(bmis)


if __name__ == '__main__':
    main()
