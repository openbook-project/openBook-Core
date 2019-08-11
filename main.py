import sys
import os

import util
import parser
import htmlwriter

#create the initial HTML file
def initFile(filename):
    html_file = util.constructString(
        "<!DOCTYPE html>",
        "<html lang=\"en\">",
        "<head>",
        "<title>" + filename + "</title>",
        "<meta charset=\"UTF-8\">",
        "\t<link rel = \"stylesheet\" href = \"" + filename + ".css\">",
        "\t" + util.addJs(filename + ".js"),
        "\t" + util.addJs("https://cdn.jsdelivr.net/gh/google/code-prettify@master/loader/run_prettify.js"),
        "\t" + util.addJs("https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-MML-AM_CHTML", "async"),
        "</head>",
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
        "grid-template-columns: auto minmax(auto, 800px) auto"
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
        "p,h2,ul,ol,h1,pre,a", "grid-column-start : 2",
        "grid-column-end : 3",
        "width:inherit",
        "margin:15px"
    )
    css_file += util.addCss(
        "b", "grid-column-start : 2",
        "grid-column-end : 3",
        "padding-left:15px"
    )
    css_file += util.addCss(
        "h1,h2", "margin-top:0px",
        "margin-bottom:0px"
    )
    css_file += util.addCss(
        ".background", "background-color:rgb(250, 250, 250 )"
    )
    css_file += util.addCss(
        "hr",
        "height: 1px",
        "border: 0",
        "border-top: 1px solid gray",
        "margin: 2.5px",
        "padding: 0",
        "width: 90%",
    )
    css_file += util.addCss(
        ".draggable",
        "position:absolute",
        "z-index:9",
        "border:1px solid #d3d3d3",
        "background-color:white",
        "max-width:500px"
    )

    css_file += util.addCss(
        ".ref_header",
        "cursor:move",
        "z-index:10",
        "background-color:#9c84a4",
        "color:#fff"
    )

    css_fd.write(css_file)
    css_fd.close()

    js_fd = open(filename + ".js", "w+")
    
    js_file = util.constructString(
        "function toggle(element){",
        "\tlet obj =  document.getElementById(element);",
        "\tobj.style.display = obj.style.display === 'none' ? 'block' : 'none';",
        "}\n")

    js_file += util.constructString(
        "let x_offset = 0;",
        "let y_offset = 0;\n",
        "function beginDrag(e){",
        "\tlet init = e.target;",
        "\tx_offset = e.clientX - init.style.left.substr(0, init.style.left.length - 2);",
        "\ty_offset = e.clientY - init.style.top.substr(0, init.style.top.length - 2);",
        "}\n"

        "function endDrag(e){",
        "\tlet obj = e.target.parentNode;",
        
        "\tobj.style.left = String(e.clientX - x_offset) + \"px\";",
        "\tobj.style.top = String(e.clientY - y_offset) + \"px\";",
        "}\n",
        "function dragstart_handler(e) {",
        "\te.dataTransfer.setData(\"text/plain\", e.target.innerText);",
        "}"
        )

    js_fd.write(js_file)
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