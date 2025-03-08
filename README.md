### Hexlet tests and linter status:
![Hexlet Actions Status](https://github.com/kamusia/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)
[![Github Actions Status](https://github.com/kamusia/python-project-50/actions/workflows/pyci.yml/badge.svg)](https://github.com/kamusia/python-project-50/actions/workflows/pyci.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/ebe544b7bfa431d424bb/maintainability)](https://codeclimate.com/github/kamusia/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/ebe544b7bfa431d424bb/test_coverage)](https://codeclimate.com/github/kamusia/python-project-50/test_coverage)
## Description
Difference Calculator allows you to find the differences between two files in JSON or YAML format. It provides a simple and efficient way to compare the contents of these files and highlights the discrepancies.

To get started, choose your files and follow the instructions.

## Installation
1. Clone this repository to your local machine.
```
# via HTTPS:
>> git clone https://github.com/kamusia/python-project-50.git
# or via SSH
>> git clone git@github.com:kamusia/python-project-50.git
```
2. install the package with command.
```
>> make setup
```
3. Run the program using the command.
```
# example
>> gendiff file1.json file2.json
```

## Usage
#### gendiff -h
[![asciicast](https://asciinema.org/a/mdNcJcggdOFnou8WoQUx0hroI.svg)](https://asciinema.org/a/mdNcJcggdOFnou8WoQUx0hroI)
#### gendiff *file1* *file2* (--f stylish)
[![asciicast](https://asciinema.org/a/consIqXtrSVwvUahlZ1WZi2Eg.svg)](https://asciinema.org/a/consIqXtrSVwvUahlZ1WZi2Eg)
### gendiff *file1* *file2* --f plain
[![asciicast](https://asciinema.org/a/id2SGSmDqCPgWKhEGe0Mn81oy.svg)](https://asciinema.org/a/id2SGSmDqCPgWKhEGe0Mn81oy)
### gendiff *file1* *file2* --f json
[![asciicast](https://asciinema.org/a/2KESGd7IUoWubRA6rwdp5QZXD.svg)](https://asciinema.org/a/2KESGd7IUoWubRA6rwdp5QZXD)
