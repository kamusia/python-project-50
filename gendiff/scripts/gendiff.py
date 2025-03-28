from gendiff.cli import get_args
from gendiff.generate_diff import generate_diff


def main():
    args = get_args()

    result = generate_diff(args.first_file, args.second_file, args.format)
    print(result)


if __name__ == "__main__":
    main()
