# prompt user for a vanity plate; any letters in input will be upper
# print Valid if all requirements met
# print Invalid if requirements not me
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if (
        lenght(s)
        and start_letter(s)
        and first_num(s)
        and first_num(s)
        and numbers_end(s)
    ):
        return True
    else:
        return False


# contain maximum of 6 characters (letters or numbers)
# contain minimum of 2 characters
def lenght(s):
    if 2 <= len(s) <= 6:
        return True
    else:
        return False


# no periods, spaces, or punctuation marks
def isalpha_isdecimal(s):
    for char in s:
        if not char.isalnum():
            return False
    return True


# must start with at least two letters
def start_letter(s):
    if s[0:2].isalpha():
        return True
    else:
        return False


# first number used cannot be 0
def first_num(s):
    for char in s:
        if char.isdecimal():
            if char[0] == "0":
                return False
            else:
                break
    return True


# numbers must come at the end
def numbers_end(s):
    alpha = ""
    decimal = ""
    for char in s:
        if char.isalpha():
            alpha += char
        elif char.isdecimal():
            decimal += char
    if alpha + decimal == s:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
