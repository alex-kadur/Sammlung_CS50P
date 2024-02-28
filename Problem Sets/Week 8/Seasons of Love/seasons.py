from datetime import date
import re
import sys
import inflect


p = inflect.engine()


# prompts the user for their date of birth in YYYY-MM-DD format
# print how old they are in minutes, rounded to the nearest integer, using English words instead of numerals
def main():
    date_input = input("Date of Birth: ")
    date_valid = check_date(date_input)
    age = get_age(date_valid)
    age_convert = convert_age(age)
    print(f"{age_convert.capitalize()} minutes")


# convert user input into suitable arguments for datetime.date()
# create date object from converted user input
# assumes, for simplicity, that the user was born at midnight (i.e., 00:00:00)
# catch invalid date by ValueError
# return date object
def check_date(date_input):
    date_match = re.search(r"^(\d{4})-(\d{2})-(\d{2})$", date_input)
    if date_match:
        year = int(date_match.group(1))
        month = int(date_match.group(2))
        day = int(date_match.group(3))
        try:
            date_valid = date(year, month, day)
            return date_valid
        except ValueError:
            sys.exit("Invalid date")
    else:
        sys.exit("Invalid date")


# create date object for current date using classmethod date.today()
# assumes, for simplicity, that the current time is midnight
# calculate user age by subtracting input date object from current date object
# overloaded `-` returns timedelta object
# returns timedelta (age) in days as int
def get_age(date_valid):
    date_current = date.today()
    age = date_current - date_valid
    if age.days < 0:
        sys.exit("Invalid date")
    else:
        return int(age.days)


# converts age in days to age in minutes
# converts age from numerals to English words unsing inflect
# returns age as English words
def convert_age(age):
    age_minutes = age * 24 * 60
    age_words = p.number_to_words(age_minutes, andword="")
    return age_words


if __name__ == "__main__":
    main()

