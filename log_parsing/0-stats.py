#!/usr/bin/python3
"""
Log parsing script that reads stdin line by line and computes metrics.
"""
import sys

def print_stats(file_size, status_codes):
    """
    Prints the current statistics.
    """
    print(f"File size: {file_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

def main():
    """
    Main function to parse logs and compute metrics.
    """
    total_size = 0
    status_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            try:
                parts = line.split()
                if len(parts) < 7:
                    continue

                # Extract and parse values
                file_size = int(parts[-1])
                status_code = int(parts[-2])

                total_size += file_size

                if status_code in status_count:
                    status_count[status_code] += 1

            except (ValueError, IndexError):
                # Skip lines with invalid format
                continue

            if line_count % 10 == 0:
                print_stats(total_size, status_count)

    except KeyboardInterrupt:
        # Print stats on keyboard interruption
        print_stats(total_size, status_count)
        raise

    # Final stats after EOF
    print_stats(total_size, status_count)

if __name__ == "__main__":
    main()
