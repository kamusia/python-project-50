from gendiff.main import generate_diff
import tempfile


def test_gendiff_json():
    assert generate_diff('file1.json', 'file2.json') == '''host: hexlet.io
- proxy: 123.234.53.22
- follow: False
- timeout: 50
+ timeout: 20
+ verbose: True'''


def test_gendiff_json():
    assert generate_diff('filepath1.yml', 'filepath2.yml') == '''host: hexlet.io
- proxy: 123.234.53.22
- follow: False
- timeout: 50
+ timeout: 20
+ verbose: True'''
