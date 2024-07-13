import argparse


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', help='Path to the first file')
    parser.add_argument('second_file', help='Path to the second file')
    parser.add_argument('-f', '--format', help='Set format of output')

    args = parser.parse_args()


if __name__ == "__main__":
    main()
