# set up dict with fruit calories pairs
fruit_calories = {
    "Apple": "130",
    "Avocado": "50",
    "Banana": "110",
    "Cantaloupe": "50",
    "Grapefruit": "60",
    "Grapes": "90",
    "Honeydew Melon": "50",
    "Kiwifruit": "90",
    "Lemon": "15",
    "Lime": "20",
    "Nectarine": "60",
    "Orange": "80",
    "Peach": "60",
    "Pear": "100",
    "Pineapple": "50",
    "Plums": "70",
    "Strawberries": "50",
    "Sweet Cherries": "100",
    "Tangerine": "50",
    "Watermelon": "80",
}


# prompt user to input a fruit (case-insensitively)
# outputs number of calories in one portion of fruit
# ignore any input that isn’t a fruit
def main():
    fruit = input("Item: ").title()
    if fruit in fruit_calories:
        print(f"Calories:{fruit_calories[fruit]}")


main()
