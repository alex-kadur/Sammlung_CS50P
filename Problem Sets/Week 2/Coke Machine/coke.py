# define price and accepted coins
accepted = [25, 10, 5]
price = 50


def main():
    # set initial balance to 0
    balance = 0
    # each time inform user of the amount due
    while balance < price:
        amount_due(balance)
        coin = insert_coin(balance)
        balance += coin
    # if user has inputted at least 50 cents > output cents user is owed
    if balance >= price:
        change_owed(balance)


# inform user of the amount due
def amount_due(balance):
    print("Amount due: ", price - balance)


# output cents user is owed
def change_owed(balance):
    print("Change owed:", balance - price)


# prompt user to insert a coin one at a time
# ignore invalid input
def insert_coin(balance):
    while True:
        coin = int(input("Insert coin: "))
        # ignore any integer that isn’t: 25 cents, 10 cents, and 5 cents; output amount due if invalid
        if coin in accepted:
            break
        else:
            amount_due(balance)
    return coin


main()
