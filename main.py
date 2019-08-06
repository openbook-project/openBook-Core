import sys
import os

import util
import parser
import htmlwriter

#create the initial HTML file
def initFile(filename):
    html_file = util.constructString(
        "<!DOCTYPE html>",
        "<html>",
        "\t<link rel = \"stylesheet\" href = \"" + filename + ".css\">",
        "\t" + util.addJs(filename + ".js"),
        "\t" + util.addJs("https://cdn.jsdelivr.net/gh/google/code-prettify@master/loader/run_prettify.js"),
        "<body>"
    )

    html_file += util.constructString(
        "<div class = \"background\"" + htmlwriter.buildStyleString("grid-row-start:1",
                                                                        "grid-row-end:100") + "></div>",
        "<div class = \"background\""+ htmlwriter.buildStyleString("grid-column-start:3",
                                             "grid-row-start:1",
                                             "grid-row-end:100") + "></div>"
    )

    html_fd = open(filename + ".html", "w+")
    html_fd.write(html_file)

    css_fd = open(filename + ".css", "w+")

    css_file = util.addCss(
        "html", "font-family: Arial, Helvetica, sans-serif;line-height: 2;"
    )
    #add the media query for the body
    css_file += util.addMediaQuery(
        "1600", "10000",
        "body", "display:grid",
        "grid-template-columns: auto 800px auto"
    )
    css_file += util.addMediaQuery(
        "1280", "1599",
        "body", "display:grid",
        "grid-template-columns: 350px auto 350px"
    )
    css_file += util.addMediaQuery(
        "1025", "1280",
        "body", "display:grid",
        "grid-template-columns: 100px auto 100px"
    )
    css_file += util.addMediaQuery(
        "768", "1024",
        "body", "display:grid",
        "grid-template-columns: 50px auto 50px"
    )
    css_file += util.addMediaQuery(
        "481", "767", "body", "display:grid",
        "grid-template-columns: 25px auto 25px"
    )
    css_file += util.addMediaQuery(
        "320", "480", "body", "display:grid",
        "grid-template-columns: 10px auto 10px"
    )
    css_file += util.addCss(
        "p,h2,ul,ol,h1,pre", "grid-column-start : 2",
        "grid-column-end : 3",
        "width:inherit",
        "margin:15px"
    )
    css_file += util.addCss(
        "h1,h2", "margin-top:0px",
        "margin-bottom:0px"
    )
    css_file += util.addCss(
        ".background", "background-color:rgb(250, 250, 250 )"
    )

    css_fd.write(css_file)
    css_fd.close()

    js_fd = open(filename + ".js", "w+")
    js_fd.close()
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