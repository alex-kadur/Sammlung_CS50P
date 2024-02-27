# output the user’s grocery list
# prefixing each line with number of times user inputted item
# avoid or catch any KeyError
def main():
    items_list = input_items()
    sorted_list = sort_list(items_list)
    for item in sorted_list:
        print(item[1], item[0])


# promt user for items, one per line
# treat user’s input case-insensitively
# store input all uppercase
# continue until user inputs control-d
# detect by catching an EOFError
def input_items():
    items_list = {}
    while True:
        try:
            item = input().upper()
            if item in items_list:
                items_list[item] += 1
            else:
                items_list[item] = 1
        except EOFError:
            return items_list


# sort output alphabetically by item
def sort_list(n):
    sorted_list = sorted(n.items())
    return sorted_list


main()
