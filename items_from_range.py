import argparse
import sys


def check_version():
    version_main, version_sub = sys.version_info[0], sys.version_info[1]
    if version_main < 3:
        sys.exit('Python version must be 3.6 or later.')
    elif version_main == 3:
        if version_sub < 6:
            sys.exit('Python version must be 3.6 or later.')


if __name__ == "__main__":
    check_version()
    from functions import items_from_range, items_from_ranges
    parser = argparse.ArgumentParser()
    parser.add_argument('type', type=str,
                        help='Range ranges or single range, args are range or single')
    parser.add_argument('range', type=str,
                        help='Enter a range like this 500-5001')

    args = parser.parse_args()
    if args.type == 'single':
        items_from_range(args.range)
    elif args.type == 'range':
        items_from_ranges(args.range)
