import sys
from tabulate import tabulate
import csv


# executes get_file_name() and stores return value as file_name
# passes file_name into get_tableand stores return value as table
# outputs table formatted as ASCII art using tabulate
# formats table using library’s grid format
def main():
    file_name = get_file_name()
    table = get_table(file_name)
    print(tabulate(table, headers="firstrow", tablefmt="grid"))


# expects exactly 1 command-line argument = name (or path) of CSV file
# if not exactly 1 command-line argument: exit via sys.exit "Too few command-line arguments" or "Too many command-line arguments"
# if specified file’s name does not end in .csv: exit via sys.exit "Not a CSV file"
def get_file_name():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1].endswith(".csv") == False:
        sys.exit("Not a CSV file")
    else:
        return sys.argv[1]
