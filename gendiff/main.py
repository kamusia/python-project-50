import json
from gendiff.diff import get_diff


def generate_diff(first_file, second_file):
    read_first, read_second = json.load(
        open(first_file)), json.load(open(second_file)
                                     )
    diff = get_diff(read_first, read_second)
    return diff
