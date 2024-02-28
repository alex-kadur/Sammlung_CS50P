import re
import sys


# takes user input in form of HTML string that should contain iframe tag with YouTube video URL
# calls parse() function to extract video ID from input string
# prints result returned by parse() function
def main():
    s = input("HTML: ")
    print(parse(s))


# uses re.search() function from re module to search for specific pattern in input string s
# looks for iframe tag that contains a YouTube video URL in the src attribute
# captures video ID from the YouTube URL
# if input contains valid YouTube video iframe: transforms and returns URL as "youtu.be" format
# if not valid: returns the string "None"
def parse(s):
    URL = re.search(
        r'^<iframe.*src="https?://(?:www.)?youtube.com/embed/(.*?)".*></iframe>$', s
    )
    if URL:
        return f"https://youtu.be/{URL.group(1)}"
    else:
        return "None"


if __name__ == "__main__":
    main()
