import re
import sys


# expects an IPv4 address as input as a str
# stores input as variable "ip"
# prints return value of validate(ip)
def main():
    ip = input("IPv4 Address: ").strip()
    print(validate(ip))


# if that input is a valid IPv4 address: returns True
# if that input is not a valid IPv4 address: returns False
def validate(ip):
    if re.search(
        r"^((25[0-5]|2[0-4][0-9]|1?[0-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1?[0-9]?[0-9])$",
        ip,
    ):
        return True
    else:
        return False


if __name__ == "__main__":
    main()
