# prompt user for str of text
# outputs same text without all vowels
# whether inputted in uppercase or lowercase

vowels = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]


def main():
    input_vowels = input("Input: ").strip()
    print("Output:", omitt_vowels(input_vowels))


# A, E, I, O, and U omitted


def omitt_vowels(input_vowels):
    # create empty str "vowels_omitted" that can later be returned
    vowels_omitted = ""
    # iterate over characters in "input_vowels" str in a loop
    for character in input_vowels:
        # add character to "vowels_omitted" if no vowel
        if character not in vowels:
            vowels_omitted += character
    return vowels_omitted


main()
