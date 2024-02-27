import inflect

# set up inflect
p = inflect.engine()

# set up empty list of names
names = []


def main():
    # prompt user for names, one per line, until the user inputs control-d
    # assume that the user will input at least one name
    try:
        while True:
            name = input("Name: ")
            # add names to list of names
            names.append(name)
    except EOFError:
        # bid adieu to those names, separating two names with one and, three names with two commas and one and, and n names with n-1 commas and one and
        # eg. "Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl"
        names_convert = p.join((names))
        print("Adieu, adieu, to " + names_convert)


if __name__ == "__main__":
    main()
