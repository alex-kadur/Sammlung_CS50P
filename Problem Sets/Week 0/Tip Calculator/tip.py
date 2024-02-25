def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

#remove leading $ and return the amount as float
def dollars_to_float(d):
    return float(d.removeprefix("$"))

#remove trailing % and return the percentage as float
def percent_to_float(p):
    return float(p.removesuffix("%")) / 100

main()
