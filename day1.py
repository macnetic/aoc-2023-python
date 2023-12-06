from os import error

import requests

from aoc_utils import get_input


# Input for today's problem
input_url = "https://adventofcode.com/2023/day/1/input"

# Global parameters
stripchars = "abcdefghijklmnopqrstuvwxyz\n"
digit_dict = {
    "oneight": "18",
    "twone": "21",
    "threeight": "38",
    "fiveight": "58",
    "sevenine": "79",
    "eightwo": "82",
    "eighthree": "83",
    "nineight": "98",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def part1():
    input_iter = get_input(input_url)
    total_sum = 0

    for input_line in input_iter:
        if input_line == "":
            continue

        digits = [s for s in input_line if s.isnumeric()]
        value = int(digits[0] + digits[-1])
        total_sum += value
        # print(f"Calibration value for the line '{input_line}' is {value}")

    return total_sum


def part2():
    input_iter = get_input(input_url)
    total_sum = 0

    for input_line in input_iter:
        if input_line == "":
            continue

        line = input_line

        for word in digit_dict:
            line = line.replace(word, digit_dict[word])

        digits = [s for s in line if s.isnumeric()]
        value = int(digits[0] + digits[-1])
        total_sum += value
        # print(f"Raw input: '{input_line}'; Processed input: '{line}'; Value: {value}")

    return total_sum


if __name__ == "__main__":
    print(part1())
    print(part2())
