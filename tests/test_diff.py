from gendiff.diff import get_diff


def test_gendiff():
    assert get_diff(
        {
            "host": "hexlet.io",
            "timeout": 50,
            "proxy": "123.234.53.22"
        },
        {
            "timeout": 20,
            "host": "hexlet.io"
        }
    ) == '''host: hexlet.io
- proxy: 123.234.53.22
- timeout: 50
+ timeout: 20'''
