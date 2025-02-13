def make_complex(value):
    _complex = (dict, set, list, tuple)
    return '[complex value]' if isinstance(value, _complex) else value


def to_str(value):
    if isinstance(value, str):
        return f"'{value}'"
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    return make_complex(value)


def make_plain_string(diff: dict, path='') -> str:
    result = ''

    for key, value in diff.items():
        new_path = path
        match value.get('type'):
            case 'added':
                result += f'Property \'{path}{key}\' was added with value: ' \
                    f'{to_str(value["value"])}\n'
            case 'changed':
                result += f'Property \'{path}{key}\' was updated. ' \
                    f'From {to_str(value["old"])} to ' \
                    f'{to_str(value["new"])}\n'
            case 'removed':
                result += f'Property \'{path}{key}\' was removed\n'
            case 'nested':
                sub_path = f'{key}.'
                new_path += sub_path
                result += make_plain_string(value['value'], new_path)
    return result


def format_plain(diff: dict) -> str:
    result = make_plain_string(diff)
    return result.rstrip('\n')
