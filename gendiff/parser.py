import json
import yaml


def parse(data, format):
    if format == 'json':
        return json.loads(data)
    elif format in ['yaml', 'yml']:
        return yaml.safe_load(data)
    else:
        raise ValueError("Unsupported format")


def open_file(file):
    with open(file, 'r') as f:
        data = f.read()

    if file.endswith('.json'):
        format = 'json'
    elif file.endswith('.yaml') or file.endswith('.yml'):
        format = 'yaml'
    else:
        raise ValueError("Unsupported file format")

    return parse(data, format)
