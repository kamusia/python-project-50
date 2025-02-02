from gendiff.diff import get_diff
from gendiff.parser import parse
from gendiff.views.stylish import format_stylish
from gendiff.views.plain import format_plain


def generate_diff(first_file, second_file, format='stylish'):
    parse_first, parse_second = parse(first_file), parse(second_file)
    diff = get_diff(parse_first, parse_second)
    match format:
        case 'stylish':
            return format_stylish(diff)
        case 'plain':
            return format_plain(diff)
