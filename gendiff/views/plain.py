def make_complex(value):
    _complex = (dict, set, list, tuple)
    return '[complex value]' if isinstance(value, _complex) else value


def gen_value(value):
    if isinstance(value, str):
        return f"'{value}'"
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    return make_complex(value)


def added(key: str, value, path: str) -> str:
    return f'Property \'{path}{key}\' was added with value: ' \
        f'{gen_value(value["value"])}\n'


def updated(key: str, value, path: str) -> str:
    return f'Property \'{path}{key}\' was updated. ' \
        f'From {gen_value(value["old"])} to ' \
        f'{gen_value(value["new"])}\n'


def generate_removed(key: str, path: str) -> str:
    return f'Property \'{path}{key}\' was removed\n'


def generate_plain_string(diff: dict, path='') -> str:
    result = ''

    for key, value in diff.items():
        new_path = path
        match value.get('type'):
            case 'added':
                result += added(key, value, path)
            case 'changed':
                result += updated(key, value, path)
            case 'removed':
                result += generate_removed(key, path)
            case 'nested':
                sub_path = f'{key}.'
                new_path += sub_path
                result += generate_plain_string(value['value'], new_path)
    return result


def format_plain(diff: dict) -> str:
    result = generate_plain_string(diff)
    return result.rstrip('\n')
