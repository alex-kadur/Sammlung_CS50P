#implement function called main; prompts user for input; calls convert on input; prints result
def main():
    faces = input()
    print(convert(faces))

#implement function called convert; returns input `:)` converted to 🙂 and `:(` converted to 🙁
def convert(x):
    return x.replace(":)", "🙂").replace(":(", "🙁")

#call main
main()
