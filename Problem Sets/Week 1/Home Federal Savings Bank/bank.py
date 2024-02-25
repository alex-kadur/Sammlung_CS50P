# prompt user for greeting and output response
# treat greeting space/case-insensitively


def main():
    greeting = input("Greeting: ").lower().strip()
    print(response(greeting))


# if greeting starts with "hello", return $0
# if greeting starts with an "h" but not "hello", return $20
# else return $100


def response(n):
    if n.startswith("hello"):
        return "$0"
    elif n.startswith("h"):
        return "$20"
    else:
        return "$100"


main()
