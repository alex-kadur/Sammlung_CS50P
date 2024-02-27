# define list of months
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


# prompt user for a date month-day-year formatted like "9/8/1636" or "September 8, 1636"
# output same date in YYYY-MM-DD format
# if input is not a valid date in either format, prompt the user again
# assume that every month has no more than 31 days
def main():
    date_user_input = input("Date: ").strip()
    try:
        if "/" in date_user_input:
            converted_date = convert_format_a(date_user_input)
            if converted_date != False:
                print(converted_date)
            else:
                main()
        elif "," in date_user_input:
            converted_date = convert_format_b(date_user_input)
            if converted_date != False:
                print(converted_date)
            else:
                main()
        else:
            main()
    except ValueError:
        pass


# convert date formatted like "9/8/1636"
# to same date in YYYY-MM-DD format
def convert_format_a(date_user_input):
    try:
        # split / m, d, y
        date_split = date_user_input.split("/")
        month, day, year = date_split
        # format A e.g. 9/8/1636
        # check 1 <= int(m) <= 12
        # check 1 <= int(d) <= 31
        # check 0 <= int(y) <= 9999
        if 1 <= int(month) <= 12 and 1 <= int(day) <= 31 and 0 <= int(year) <= 9999:
            # return yyyy-mm-dd
            return f"{int(year):04}-{int(month):02}-{int(day):02}"
        else:
            return False
    except ValueError:
        return False


# convert date formatted like "September 8, 1636"
# to same date in YYYY-MM-DD format
def convert_format_b(date_user_input):
    try:
        # split / m, d, y
        date_format = date_user_input.replace(" ", "/", 1).replace(", ", "/", 2)
        date_split = date_format.split("/")
        month, day, year = date_split
        if month in months:
            # format B e.g. September 8, 1636
            # check 1 in months
            # check 1 <= int(d) <= 31
            # check 0 <= int(y) <= 9999
            month_digit = convert_month(month)
            if 1 <= int(day) <= 31 and 0 <= int(year) <= 9999:
                # return yyyy-mm-dd
                return f"{int(year):04}-{int(month_digit):02}-{int(day):02}"
            else:
                return False
        else:
            return False
    except ValueError:
        return False


# convert motnh from str to digit
def convert_month(month):
    month_digit = months.index(month) + 1
    return month_digit


main()
