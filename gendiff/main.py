import json
import yaml  # type: ignore
from gendiff.diff import get_diff


def generate_diff(first_file, second_file):
    read_first, read_second = read_file(first_file), read_file(second_file)
    diff = get_diff(read_first, read_second)
    return diff


def read_file(file):
    if file.endswith('.json'):
        return json.load(open(file))
    elif file.endswith('.yaml') or file.endswith('.yml'):
        return yaml.safe_load(open(file))
    else:
        raise ValueError("Unsupported file format")
