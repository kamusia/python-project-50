from gendiff.diff import get_diff
from gendiff.parser import parse
from gendiff.views.stylish import format_stylish


def generate_diff(first_file, second_file, format='stylish'):
    parse_first, parse_second = parse(first_file), parse(second_file)
    diff = get_diff(parse_first, parse_second)
    match format:
        case 'stylish':
            return format_stylish(diff)
