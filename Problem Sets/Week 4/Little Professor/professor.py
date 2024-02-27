import random


# calls get_level() and stores return value
# calls and passes level into math_problem()
# counts problems_total and problems_right
# after 10 problems outputs user’s score "Score: ": the number of correct answers out of 10
def main():
    problems_total = 0
    problems_right = 0
    level = get_level()
    while problems_total < 10:
        total_count, right_count = math_problem(level)
        problems_total += total_count
        problems_right += right_count
    print(f"Score: {problems_right}")


# prompts user for a level n "Level: "
# if user does not input 1, 2, or 3: prompts again
def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if 1 <= n <= 3:
                return n
        except ValueError:
            pass


# returns a randomly generated non-negative integer with n level digits or raises a ValueError if level is not 1, 2, or 3
def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError


# randomly generates math problems formatted as "X + Y =", each of X and Y is a non-negative integer with n digits
# prompts user to solve each problem
# if answer is correct: returns 1 problem/1 right
# if answer is not correct (or not even a number): outputs "EEE" and prompt user again, allowing user up to three tries in total for each problem
# if user has still not answered correctly after three tries: outputs correct answer "X + Y = Z", returns 1 problem/0 right
def math_problem(level):
    X = generate_integer(level)
    Y = generate_integer(level)
    Z = int(X + Y)
    tries = 0
    while tries < 3:
        answer = int(input(f"{X} + {Y} = "))
        if answer == Z:
            return (1, 1)
        else:
            print("EEE")
            tries += 1
            pass
    print(f"{X} + {Y} = {Z}")
    return (1, 0)


if __name__ == "__main__":
    main()
