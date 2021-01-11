import sys


def items_from_range(values: str) -> str:
    """Function to convert a range into a joined string of items

    Args:
        start (int): Start of range
        end (int): End of Range

    Returns:
        str: string of range items seperated by a comma
    """
    try:
        start, end = values.split('-')
    except ValueError:
        sys.exit(
            'Input not in correct format, must be a range seperate with a hyphen')

    # Convert Values
    print((',').join([str(x) for x in list(range(int(start), int(end)+1))]))


def items_from_ranges(values: str) -> str:
    """Function to convert a range into a joined string of items

    Args:
        start (int): Start of range
        end (int): End of Range

    Returns:
        str: string of range items seperated by a comma
    """
    try:
        ranges = values.split(',')
    except ValueError:
        sys.exit(
            'Input not in correct format, must be a range seperate with a comma')

    formatted_ranges = []
    for item in ranges:
        if '-' in item:
            try:
                start, end = item.split('-')
            except ValueError:
                sys.exit(
                    'Input not in correct format, must be a range seperate with a hyphen')

            formatted_ranges.extend(
                [str(x) for x in list(range(int(start), int(end)+1))])
        else:
            formatted_ranges.append(str(item))
    # Convert Values
    print('\n\n')
    print((',').join(formatted_ranges))
    print('\n\n')
