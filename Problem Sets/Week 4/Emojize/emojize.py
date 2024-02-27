# prompt user for a str in English
# convert any codes (or aliases) therein to their corresponding emoji
# output the “emojized” version of that str

from emoji import emojize


# prompt user for a str in English
# output the “emojized” version of that str
def main():
    EmojiI = input("Input: ")
    EmojiO = convert(EmojiI)
    print("Output: " + EmojiO)


# convert any codes (or aliases) therein to their corresponding emoji
def convert(EmojiI):
    return emojize(EmojiI)


if __name__ == "__main__":
    main()
