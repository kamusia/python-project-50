from gendiff.diff import get_diff
from gendiff.parser import open_file_and_parse
from gendiff.views.format import match_format


def generate_diff(first_file, second_file, format='stylish'):
    parse_first, parse_second = open_file_and_parse(
        first_file), open_file_and_parse(second_file)
    diff = get_diff(parse_first, parse_second)
    return match_format(diff, format)
