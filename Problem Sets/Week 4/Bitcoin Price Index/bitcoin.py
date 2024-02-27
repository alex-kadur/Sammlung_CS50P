import sys
import requests
import json


# calls get_n() for number of BTC User would like to buy
# calls get_price() for current BTC price from api.coindesk.com
# multiplies n with price
# outputs the current cost of n Bitcoins in USD (four decimal places,"," as thousands separator)


def main():
    n = get_n()
    price = get_price()
    result = n * price
    print(f"${result:,.4f}")


# expects user to specify as command-line argument number n
# if argument cannot be converted to float: exits via sys.exit, error message ("Missing command-line argument", "Command-line argument is not a number")
def get_n():
    try:
        n = float(sys.argv[1])
    except IndexError:
        sys.exit("Missing command-line argument")
    except ValueError:
        sys.exit("Command-line argument is not a number")
    return n


# API for CoinDesk Bitcoin Price Index at https://api.coindesk.com/v1/bpi/currentprice.json returns JSON
# catch exceptions, with code like: except requests.RequestException
# returns current BTC price in USD from nested keys as float
def get_price():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    except requests.RequestException:
        sys.exit("Failed to retrieve current BTC price")
    o = response.json()
    try:
        price = float(o["bpi"]["USD"]["rate_float"])
    except ValueError:
        sys.exit("Failed to retrieve current BTC price")
    return price


if __name__ == "__main__":
    main()
