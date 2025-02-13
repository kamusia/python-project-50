from collections import OrderedDict


def get_diff(dict1, dict2):
    keys = sorted(set(dict1.keys()).union(dict2.keys()))
    diff = {}

    for i in keys:
        if isinstance(dict1.get(i), dict) and isinstance(dict2.get(i), dict):
            diff[i] = {'type': 'nested',
                       'value': get_diff(dict1[i], dict2[i])}
        elif i not in dict1.keys():
            diff[i] = {'type': 'added', 'value': dict2[i]}
        elif i not in dict2.keys():
            diff[i] = {'type': 'removed', 'value': dict1[i]}
        elif dict1[i] == dict2[i]:
            diff[i] = {'type': 'unchanged', 'value': dict1[i]}
        else:
            diff[i] = {'type': 'changed', 'old': dict1[i], 'new': dict2[i]}

    return OrderedDict(sorted(diff.items()))
