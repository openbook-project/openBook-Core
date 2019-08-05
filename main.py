import sys
import os

import util
import parser

#create the initial HTML file
def initFile(filename):
    html_file = util.constructString(
        "<!DOCTYPE html>",
        "<html>",
        "\t<link rel = \"stylesheet\" href = \"" + filename + ".css\">"
        "<body>"
    )

    html_fd = open(filename + ".html", "w+")
    html_fd.write(html_file)

    css_fd = open(filename + ".css", "w+")

    css_file = util.addCss(
        "html", "font-family: Arial, Helvetica, sans-serif;line-height: 1.5;"
    )
    css_file += util.addCss(
        "body", "display:grid",
        "grid-template-columns: 150px auto 150px",
        "grid-template-rows: auto",
        "align-items: center",
    )
    css_file += util.addCss(
        "p,h2,ul,ol,h1", "grid-column-start : 2",
        "grid-column-end : 3"
    )
    css_file += util.addCss(
        "h1", "margin:5px"
    )

    css_fd.write(css_file)
    css_fd.close()

    return html_fd

def main():
    #get the name of the file to parse
    filename = ''
    if(len(sys.argv) < 2):
        filename = input("enter a .book file to parse\n")
    else:
        filename = sys.argv[1]

    #try and open the file
    try:
    	fd = open(filename, "r")
    except IOError:
        print("Could not open " + filename)
        sys.exit(1)

    #remove path and extension from filename
    file_location = os.path.basename(filename)
    filename = os.path.splitext(file_location)[0]

    #create directories for book if they don't exist
    if not os.path.exists(filename):
        os.mkdir(filename)

    os.chdir(filename)
    html_fd = initFile(filename)

    parser.parse(html_fd, fd)


if __name__ == "__main__":
	main()