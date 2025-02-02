import pytest
from gendiff.main import generate_diff

json_old = 'tests/fixtures/file1.json'
json_new = 'tests/fixtures/file2.json'
yaml_old = 'tests/fixtures/file1.yml'
yaml_new = 'tests/fixtures/file2.yml'
json_old2 = 'tests/fixtures/nested_file1.json'
json_new2 = 'tests/fixtures/nested_file2.json'
yml_old2 = 'tests/fixtures/nested_file1.yml'
yml_new2 = 'tests/fixtures/nested_file2.yml'
stylish = 'tests/fixtures/stylish'
nested_stylish = 'tests/fixtures/nested_stylish'
plain = 'tests/fixtures/plain'


@pytest.mark.parametrize(
    'path1, path2, format, expected',
    [
        (json_old, json_new, 'stylish', stylish),
        (yaml_old, yaml_new, 'stylish', stylish),
        (json_old2, json_new2, 'stylish', nested_stylish),
        (yml_old2, yml_new2, 'stylish', nested_stylish),
        (json_old, json_new, 'plain', plain),
        (yaml_old, yaml_new, 'plain', plain),
        (json_old2, json_new2, 'plain', plain),
        (yml_old2, yml_new2, 'plain', plain),
    ]
)
def test_gendiff(path1, path2, format, expected):
    with open(expected) as f:
        assert generate_diff(path1, path2, format) == f.read()
