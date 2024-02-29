from fpdf import FPDF
from fpdf.enums import Align


def main():
    # creates instance of FPDF class
    # orientation is Portrait (default)
    # unit is mm (default)
    # format is A4 (210mm wide by 297mm tall) (default)
    shirtificate = FPDF()
    # adds a new page to the PDF
    shirtificate.add_page()
    # prints the title calling print_title
    print_title(shirtificate)
    # adds an image to the PDF (shirt)
    # y position is set to 80
    # width is set to 180
    # x position is aligned to center of the page
    shirtificate.image(
        y=80,
        name="shirtificate.png",
        w=180,
        x=Align.C,
    )
    # prints the text on the shirt calling print_text_shirt
    print_text_shirt(shirtificate)
    # saves PDF to file "shirtificate.pdf"
    shirtificate.output("shirtificate.pdf")


def print_title(shirtificate):
    # sets y position to 30mm from top
    shirtificate.set_y(30)
    # sets font to helvetica, bold, size 50
    shirtificate.set_font("helvetica", style="B", size=50)
    # adds a cell with a widht of 180 and height 25 and text centered
    shirtificate.cell(w=180, h=25, txt="CS50 Shirtificate", center=True, align=Align.C)


def print_text_shirt(shirtificate):
    # prompts user for a name and stores input as name
    name = input("Name: ")
    # sets y position to 130mm from top
    shirtificate.set_y(130)
    # sets font to helvetica, bold, size 24
    shirtificate.set_font("helvetica", style="B", size=24)
    # sets font color to white
    shirtificate.set_text_color(255, 255, 255)
    # adds a cell with a widht of 180 and height 25 and text centered
    shirtificate.cell(w=180, h=25, txt=f"{name} took CS50", center=True, align=Align.C)


if __name__ == "__main__":
    main()
