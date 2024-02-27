import sys
import csv


# executes get_file_names() and stores return values as file_name_input and file_name_output
# passes file_name_input into get_input and stores return value as input
# passes input into get_output and stores return value as output
# writes output to file using DictWriter
# writes fieldnames to file using writeheader with no arguments
def main():
    file_name_input, file_name_output = get_file_names()
    input = get_input(file_name_input)
    output = get_output(input)
    with open(file_name_output, "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        writer.writerows(output)


# expects user to provide 2 command-line arguments
# 1st argument = name of existing CSV file as input, columns in order, "name" and "house"
# 2nd argument = name of new CSV as output, columns in order, "first", "last" and "house"
# if user does not provide exactly 2 command-line arguments: exit via sys.exit "Too few command-line arguments" or "Too many command-line arguments"
# if first argument cannot be read: exit via sys.exit "Could not read invalid_file.csv"
def get_file_names():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1].endswith(".csv") == False:
        sys.exit("Could not read invalid_file.csv")
    else:
        return sys.argv[1], sys.argv[2]


# tries to open file specified by input
# if specified file does not exist: FileNotFoundError and exits via sys.exit "File does not exist"
# uses csv.DictReader to append content CSV to list input_read, columns order: "name" and "house"
# returns input_read
def get_input(file_name_input):
    input_read = []
    try:
        with open(file_name_input) as file:
            reader = csv.DictReader(file)
            for row in reader:
                input_read.append({"name": row["name"], "house": row["house"]})
    except FileNotFoundError:
        sys.exit("File does not exist")
    return input_read


# takes "input" list as input column order: "name" and "house"
# creates empty output list "output"
# loops throug input list "input"
# for every input_item (dict) splits input_item["name"]  at ", " into 2 values stored as list "input_split"
# stores input_split[0] as "last" and input_split[1] as "first"
# creates output_item (dict) using first, last and input_item["house"]
# appends output_item to initialy empty output list
# returns "output" list with column order: "first", "last" and "house"
def get_output(input):
    output = []
    for input_item in input:
        input_split = input_item["name"].split(", ")
        first = input_split[1]
        last = input_split[0]
        output_item = {"first": first, "last": last, "house": input_item["house"]}
        output.append(output_item)
    return output


if __name__ == "__main__":
    main()
