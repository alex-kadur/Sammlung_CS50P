from random import randint


def main():
    # prompt user for a level n "Level: "
    level = get_positive_integer("Level: ")
    # randomly generate integer between 1 and n, use "random" module
    random_number = randint(1, level)
    while True:
        # prompt user to guess the integer "Guess: "
        guess = get_positive_integer("Guess: ")
        # if guess is smaller than that integer, output "Too small!" and prompt user again
        if guess < random_number:
            print("Too small!")
            pass
        # if guess is larger than that integer, output "Too large!" and prompt user again
        elif guess > random_number:
            print("Too large!")
            pass
        # if guess is the same as that integer, output: "Just right!" and exit
        else:
            print("Just right!")
            break


# prompt user for input
# if user does not input a positive integer, prompt again
def get_positive_integer(prompt):
    while True:
        try:
            n = int(input(prompt))
            if n > 0:
                return n
        except ValueError:
            pass


if __name__ == "__main__":
    main()
