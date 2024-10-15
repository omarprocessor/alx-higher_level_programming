#!/usr/bin/python3
"""Script to compute metrics from log entries
"""

import sys


def print_stats(total_size, status_codes):
    """Prints the total file size and the number of lines by status code."""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


def main():
    """Main function to read from stdin and compute metrics."""
    total_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0,
                    403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1

            # Split the line to extract file size and status code
            parts = line.split()
            if len(parts) >= 7:
                try:
                    file_size = int(parts[-1])
                    status_code = int(parts[-2])
                    total_size += file_size

                    # Update status code count
                    if status_code in status_codes:
                        status_codes[status_code] += 1
                except (ValueError, IndexError):
                    continue

            # Print stats every 10 lines
            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)


if __name__ == "__main__":
    main()
