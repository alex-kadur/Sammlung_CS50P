# assumes that any line that starts with # is a comment
# assumea that any line that only contains whitespace is blank
# use str methos startswith and lstrip
# open can raise FileNotFoundError


import sys


# executes get_file_name() and stores return value as file_name
# passes file_name into get_lines_code and stores return value as lines_code
# outputs lines_code
def main():
    file_name = get_file_name()
    lines_code = get_lines_code(file_name)
    print(lines_code)


# expects exactly 1 command-line argument: name (or path) of a Python file
# if not exactly 1 command-line argument: exit via sys.exit "Too few command-line arguments" or exit via sys.exit "Too many command-line arguments" or "Not a Python file"
# if specified file’s name does not end in .py: exit via sys.exit "Not a Python file"
def get_file_name():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1].endswith(".py") == False:
        sys.exit("Not a Python file")
    else:
        return sys.argv[1]


# tries to open file specified by input
# if specified file does not exist: exits via sys.exit "File does not exist"
# loops over lines in file and adds +1 to line_count for every valid line
# returns line_count, excluding comments (#) and blank lines
def get_lines_code(file_name):
    line_count = 0
    try:
        with open(file_name) as file:
            for line in file:
                stripped_line = line.strip()
                if stripped_line.startswith("#") or stripped_line == "":
                    pass
                else:
                    line_count += 1
    except FileNotFoundError:
        sys.exit("File does not exist")
    return line_count


if __name__ == "__main__":
    main()
