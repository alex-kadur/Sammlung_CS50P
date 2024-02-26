# prompt user for name of a variable in camel case
# outputs corresponding name in snake cases


def main():
    camel = input("camelCase: ").strip()
    snake = snake_case(camel)
    print(f"snake_case: {snake}")


# convert camel case to snake case


def snake_case(camel):
    # create empty str "snake" that can later be returned
    snake = ""
    # iterate over characters in "camel" str in a loop
    for character in camel:
        # add _character.lower to "snake" if character is.upper
        if (character).isupper() == True:
            snake = snake + f"_{character.lower()}"
        # add character to "snake" if character is.lower
        else:
            snake = snake + character
    return snake.strip("_")


main()
