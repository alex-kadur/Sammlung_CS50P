import re
import sys


def main():
    print(count(input("Text: ")))


# expects a line of text as input as a str
# returns, as an int, the number of times that “um” appears in that text case-insensitively
# only as a word unto itself, not as a substring of some other word
# use re findall
# \b is “defined as the boundary between a \w and a \W character (or vice versa), or between \w at the beginning/end of the string
def count(s):
    um = re.findall(r"\bum\b", s.lower())
    count_um = len(um)
    return count_um


if __name__ == "__main__":
    main()
