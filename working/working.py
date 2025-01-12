import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    # Define the pattern to match the input format
    pattern = r'^\s*(\d{1,2}(:\d{2})?)\s*(AM|PM)\s*to\s*(\d{1,2}(:\d{2})?)\s*(AM|PM)\s*$'
    match = re.match(pattern, s, re.IGNORECASE)

    # Raise ValueError if the format is incorrect
    if not match:
        raise ValueError("Invalid time format")

    start_time, _, start_period, end_time, _, end_period = match.groups()

    # Convert both start and end times to 24-hour format
    start_24 = convert_to_24_hour_format(start_time, start_period)
    end_24 = convert_to_24_hour_format(end_time, end_period)

    return f"{start_24} to {end_24}"


def convert_to_24_hour_format(time, period):
    hours, minutes = (time.split(':') + ["00"])[:2]  # Default to "00" if minutes are not provided
    hours = int(hours)
    minutes = int(minutes)

    # Validate minutes
    if minutes < 0 or minutes >= 60:
        raise ValueError("Invalid minutes")

    if period.upper() == "AM":
        if hours == 12:
            hours = 0  # Midnight case
        elif hours < 1 or hours > 11:
            raise ValueError("Invalid hour for AM")
    elif period.upper() == "PM":
        if hours == 12:
            hours = 12  # Noon case
        elif hours < 1 or hours > 11:
            raise ValueError("Invalid hour for PM")
        else:
            hours += 12
    else:
            raise ValueError("Invalid period")

    return f"{hours:02}:{minutes:02}"


if __name__ == "__main__":
    main()
