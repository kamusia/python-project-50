from gendiff.diff import get_diff
from gendiff.parser import parse


def generate_diff(first_file, second_file):
    parse_first, parse_second = parse(first_file), parse(second_file)
    diff = get_diff(parse_first, parse_second)
    return diff
