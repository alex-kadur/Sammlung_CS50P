import sys
from PIL import Image, ImageOps


# executes get_file_names() and stores return values as file_name_input and file_name_output
def main():
    file_name_input, file_name_output = get_file_names()
    input = file_name_input
    output = file_name_output
    image_shirt(input, output)


# expects exactly two command-line arguments:
# in sys.argv[1], the name (or path) of a JPEG or PNG to read (i.e., open) as input
# in sys.argv[2], the name (or path) of a JPEG or PNG to write (i.e., save) as output
# exit via sys.exit:
# if the user does not specify exactly two command-line arguments
# Too few command-line arguments
# Too many command-line arguments
# if the input’s and output’s names do not end in .jpg, .jpeg, or .png, case-insensitively
# "Invalid input/output"
# if the input’s name does not have the same extension as the output’s name
# "Input and output have different extensions"
def get_file_names():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        arg_1 = str(sys.argv[1].lower())
        arg_2 = str(sys.argv[2].lower())
        extensions = (".jpg", ".jpeg", ".png")
        if arg_1.endswith(extensions) == False:
            sys.exit("Invalid input")
        elif arg_2.endswith(extensions) == False:
            sys.exit("Invalid output")
        elif arg_1.rsplit(".")[-1] != arg_2.rsplit(".")[-1]:
            sys.exit("Input and output have different extensions")
        else:
            return arg_1, arg_2


# Open the input with Image.open
# resize the input with ImageOps.fit
# using default values for method, bleed, and centering, overlay the shirt with Image.paste
# save the result with Image.save
def image_shirt(input, output):
    try:
        i_shirt = Image.open("shirt.png")
        shirt_width, shirt_height = i_shirt.size

        i_input = Image.open(input)
        i_input = ImageOps.fit(i_input, (shirt_width, shirt_height))

        i_input.paste(i_shirt, (0, 0), mask=i_shirt)
        i_input.save(output)

    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
