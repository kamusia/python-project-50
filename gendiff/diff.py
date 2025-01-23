from collections import OrderedDict


def get_diff(dict1, dict2):
    keys = list(OrderedDict.fromkeys(list(dict1.keys()) + list(dict2.keys())))
    unchanged, deleted, changed, added = [], [], [], []

    for key in keys:
        if dict1.get(key) == dict2.get(key):
            unchanged.append(f"{key}: {dict1[key]}")
        if key not in dict2:
            deleted.append(f"- {key}: {dict1[key]}")
        elif key not in dict1:
            added.append(f"+ {key}: {dict2[key]}")
        elif dict1.get(key) != dict2.get(key):
            changed.append(f"- {key}: {dict1[key]}\n+ {key}: {dict2[key]}")

    diff = unchanged + deleted + changed + added
    return str('\n'.join(diff))
