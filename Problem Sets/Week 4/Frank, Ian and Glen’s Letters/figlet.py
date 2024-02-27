from pyfiglet import Figlet
from random import choice
import sys


figlet = Figlet()

# get a list of available fonts with:
Fonts = figlet.getFonts()


# set the font
# prompt the user for a str of text
# outputs text in desired font
def main():
    Font = CheckInput()
    figlet.setFont(font=Font)
    Text = input("Input: ")
    print("Output:\n\n" + figlet.renderText(Text))


# expect 0 or 2 command-line arguments
# 0 if user would like to output text in a random font
# 2 if user would like to output text in a specific font
# 1st of 2 should be -f or --font
# 2nd of 2 should be name of the font
# if 1st is not -f or --font exit via sys.exit with error message
# if 2nd is not the name of a font exit via sys.exit with error message
def CheckInput():
    if len(sys.argv) == 1:
        return choice(Fonts)
    elif len(sys.argv) == 3:
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            if sys.argv[2] in Fonts:
                return sys.argv[2]
            else:
                print(Fonts)
                sys.exit("second argument must be one of these fonts")
        else:
            sys.exit("first argument must be '-f' or '--font'")
    else:
        sys.exit("0 or 2 command-line arguments expected")


if __name__ == "__main__":
    main()
