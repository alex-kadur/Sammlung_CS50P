#prompt user for `m` kilograms and output equivalent `E` Joules
def main():
    joules = int(input("m: "))
    print("E:", emc2(joules))

#calculate equivalent number Joules via E=mc2
def emc2(m):
    c2 = pow(300000000,2)
    return m * c2

#call main
main()
