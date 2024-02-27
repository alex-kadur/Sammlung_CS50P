vowels = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]


# prompt user for str of text (ignores empty)
# outputs same text without all vowels
def main():
    word = input("Input: ").strip()
    word_out = shorten(word)
    print(f"Output: {word_out}")


# takes str as input and returns same str with A, E, I, O, U omitted
def shorten(word):
    # create empty str "vowels_omitted" that can later be returned
    vowels_omitted = ""
    # iterate over characters in "input_vowels" str in a loop
    for character in word:
        # add character to "vowels_omitted" if no vowel
        if character not in vowels:
            vowels_omitted += character
    return vowels_omitted


if __name__ == "__main__":
    main()
