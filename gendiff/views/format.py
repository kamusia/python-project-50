from gendiff.views.stylish import format_stylish
from gendiff.views.plain import format_plain
from gendiff.views.json import format_json


def match_format(diff, format):
    match format:
        case 'stylish':
            return format_stylish(diff)
        case 'plain':
            return format_plain(diff)
        case 'json':
            return format_json(diff)
