import validators


# prompts the user for an email address via input "What's you email address? "
# prints str returned by validate()
def main():
    print(validate(input("What's you email address? ")))


# takes input from main()
# uses validators.email for validation
# returns "Valid" if: the input is a syntatically valid email address
# returns "Invalid" if: the input is not a syntatically valid email address
def validate(s):
    if validators.email(s) is True:
        return "Valid"
    else:
        return "Invalid"


if __name__ == "__main__":
    main()
