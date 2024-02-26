def main():
    percentage = get_int("Fraction: ")
    print(output(percentage))


# prompt user for a fraction, formatted as X/Y, each of X and Y is an integer
def get_int(prompt):
    while True:
        try:
            x, y = input(prompt).split("/")
            x, y = int(x), int(y)
            # if X is greater than Y instead prompt the user again
            if x > y:
                pass
            else:
                # output, as a percentage rounded to the nearest integer
                return round(x / y * 100)
        # if Y is 0 instead prompt the user again -  ZeroDivisionError
        # if X or Y is not an integer instead prompt the user again - ValueError
        except (ValueError, ZeroDivisionError):
            pass


def output(p):
    if 1 < p < 99:
        return f"{p}%"
    # if 1% or less output E instead
    elif p <= 1:
        return "E"
    # if 99% or more output F instead
    elif p >= 99:
        return "F"


main()
