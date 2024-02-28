import re
import sys

conversion_table_AM = {
    1: 1,
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 7,
    8: 8,
    9: 9,
    10: 10,
    11: 11,
    12: 0,
}

conversion_table_PM = {
    1: 13,
    2: 14,
    3: 15,
    4: 16,
    5: 17,
    6: 18,
    7: 19,
    8: 20,
    9: 21,
    10: 22,
    11: 23,
    12: 12,
}


def main():
    u_input = input("Hours: ").strip()
    time_convert = convert(u_input)
    print(time_convert)


# expects a str in 12-hour format (9:00 AM to 5:00 PM or 9 AM to 5 PM)
# returns the corresponding str in 24-hour format
# expects that AM and PM will be capitalized (with no periods therein)
# expects there will be a space before each
# raise a ValueError if:
# input to convert is not in either of the formats
# time is invalid (e.g., 12:60 AM, 13:00 PM, etc.)
def convert(s):
    t = re.search(
        r"^(1[0-2]|0?[1-9]):?([0-5][0-9])?\s(AM|PM)\sto\s(1[0-2]|0?[1-9]):?([0-5][0-9])?\s(AM|PM)$",
        s,
    )
    if t:
        start_am_pm = t.group(3)
        end_am_pm = t.group(6)
        if start_am_pm == "AM":
            start_hour = conversion_table_AM[int(t.group(1))]
        else:
            start_hour = conversion_table_PM[int(t.group(1))]
        if t.group(2) is not None:
            start_minute = int(t.group(2))
        else:
            start_minute = 0
        if end_am_pm == "AM":
            end_hour = conversion_table_AM[int(t.group(4))]
        else:
            end_hour = conversion_table_PM[int(t.group(4))]
        if t.group(5) is not None:
            end_minute = int(t.group(5))
        else:
            end_minute = 0
        return f"{start_hour:02}:{start_minute:02} to {end_hour:02}:{end_minute:02}"
    else:
        raise ValueError


if __name__ == "__main__":
    main()
