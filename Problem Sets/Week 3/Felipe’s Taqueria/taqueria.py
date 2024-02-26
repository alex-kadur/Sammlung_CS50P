menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
}


def main():
    # after each inputted item, display the total cost of all items inputted thus far, prefix $, formatted to two decimal places
    total = 0
    while True:
        try:
            item_price = validate_input()
            total += item_price
            print(f"Total: ${total:.2f}")
        # end input when user inputs control-d
        except EOFError:
            break


def validate_input():
    while True:
        try:
            # prompt user for items, one per line
            # treat user’s input case insensitively
            item = input("Item: ").title()
            # ignore any input that isn’t an item
            if item in menu:
                return float(menu[item])
            else:
                pass
        except KeyError:
            pass


main()
