# prompt user for greeting and output response
# treat greeting space/case-insensitively
def main():
    greeting = input("Greeting: ").strip()
    print(f"${value(greeting)}")


# if greeting starts with hello, return 0
# if greeting starts with h/but not hello, return 20
# else return 100
def value(greeting):
    if greeting.lower().startswith("hello"):
        return int(0)
    elif greeting.lower().startswith("h"):
        return int(20)
    else:
        return int(100)


if __name__ == "__main__":
    main()
