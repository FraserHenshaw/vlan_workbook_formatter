import argparse
from functions import format_workbook
import sys


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('path', type=str,
                        help='Path to Excel File')
    parser.add_argument('col', type=str,
                        help='Enter column to modify')

    args = parser.parse_args()

    path = args.path
    col = args.col

    format_workbook(path, col)
