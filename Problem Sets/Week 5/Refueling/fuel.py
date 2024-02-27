def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    print(gauge(percentage))


# prompt user for a fraction, formatted as X/Y, each of X and Y is an integer
# if x > y: raise ValueError
# if y == 0: raise ZeroDivisionError
# return fraction as a percentage rounded to the nearest integer
def convert(fraction):
    x, y = fraction.split("/")
    x, y = int(x), int(y)
    if y == 0:
        raise ZeroDivisionError
    elif x > y:
        raise ValueError
    else:
        return round(x / y * 100)


# if 1% or less: return E
# if 99% or more: return F
# else: return percentage in %
def gauge(percentage):
    if 1 < percentage < 99:
        return f"{percentage}%"
    elif percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"


if __name__ == "__main__":
    main()
