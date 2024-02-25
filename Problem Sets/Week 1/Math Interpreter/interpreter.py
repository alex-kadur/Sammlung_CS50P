# prompt user for arithmetic expression
# input will be formatted as x y z, with one space between
# input x and z integer; input y is +, -, *, or /
# output result as float; formatted to one decimal place


def main():
    x, y, z = input("Expession: ").split(" ")
    print(round(calculation(x, y, z), 1))


# calculate result of input


def calculation(a, b, c):
    match b:
        case "+":
            return float(a) + float(c)
        case "-":
            return float(a) - float(c)
        case "*":
            return float(a) * float(c)
        case "/":
            return float(a) / float(c)


main()
