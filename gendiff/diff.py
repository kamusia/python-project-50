from collections import OrderedDict


def get_diff(dict1, dict2):
    keys = sorted(set(dict1.keys()).union(dict2.keys()))
    diff = {}

    for key in keys:
        if (isinstance(dict1.get(key), dict)
                and isinstance(dict2.get(key), dict)):
            diff[key] = {
                'type': 'nested',
                'value': get_diff(dict1[key], dict2[key])
            }
        elif key not in dict1.keys():
            diff[key] = {'type': 'added', 'value': dict2[key]}
        elif key not in dict2.keys():
            diff[key] = {'type': 'removed', 'value': dict1[key]}
        elif dict1[key] == dict2[key]:
            diff[key] = {'type': 'unchanged', 'value': dict1[key]}
        else:
            diff[key] = {
                'type': 'changed',
                'old': dict1[key],
                'new': dict2[key]
            }

    return OrderedDict(sorted(diff.items()))
