from datetime import date
import re
import sys
import inflect


p = inflect.engine()


def main():
    date_input = input("Date of Birth: ")
    date_valid = check_date(date_input)
    age = get_age(date_valid)
    age_convert = convert_age(age)
    print(f"{age_convert.capitalize()} minutes")


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


def get_age(date_valid):
    date_current = date.today()
    age = date_current - date_valid
    if age.days < 0:
        sys.exit("Invalid date")
    else:
        return int(age.days)


def convert_age(age):
    age_minutes = age * 24 * 60
    age_words = p.number_to_words(age_minutes, andword="")
    return age_words


if __name__ == "__main__":
    main()
