# prompt user for name of a file; case/space-insensitive
# output media type
def main():
    file_name = input("File name: ").lower().strip()
    print(check_extension(file_name))


# check if there is extension

no_other = "application/octet-stream"


def check_extension(n):
    if n.find(".") == -1:
        return no_other
    else:
        name, extension = n.rsplit(".", maxsplit=1)
        return media_type(extension)


# if extension gif or jpg or jpeg or png return "image/"{extension}
# if extension pdf or zip return "application/"{extension}
# if extension txt return "txt/plain"
# if other extension return "application/octet-stream"


def media_type(n):
    match n:
        case "jpeg" | "png" | "gif":
            return f"image/{n}"
        case "pdf" | "zip":
            return f"application/{n}"
        case "jpg":
            return media_type("jpeg")
        case "txt":
            return "text/plain"
        case _:
            return no_other


main()
