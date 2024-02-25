# prompt user for answer to the Great Question of Life, the Universe and Everything
def main():
    answer = (
        input(
            "What is the answer to the Great Question of Life, the Universe and Everything? "
        )
        .strip()
        .lower()
    )
    print(response(answer))


# output Yes if user inputs 42 or (case/space-insensitively) forty-two or forty two; otherwise output No
def response(n):
    match n:
        case "42" | "forty-two" | "forty two":
            return "Yes"
        case _:
            return "No"


main()
