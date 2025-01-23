import pytest
from gendiff.main import generate_diff

json_old = 'tests/fixtures/file1.json'
json_new = 'tests/fixtures/file2.json'
yaml_old = 'tests/fixtures/file1.yml'
yaml_new = 'tests/fixtures/file2.yml'


@pytest.mark.parametrize(
    'path1, path2',
    [
        (json_old, json_new),
        (yaml_old, yaml_new)
    ]
)
def test_gendiff(path1, path2):
    assert generate_diff(path1, path2) == '''host: hexlet.io
- proxy: 123.234.53.22
- follow: False
- timeout: 50
+ timeout: 20
+ verbose: True'''
