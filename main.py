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
        "html", "font-family: Arial, Helvetica, sans-serif",
        "line-height: 2"
    )
    css_file += util.addCss(
        ":root",
        "--primary:#9c84a4",
        "--highlight:#b597bf"
    )
    #add the media query for the body
    css_file += util.addMediaQuery(
        "1600", "10000",
        "body", "display:grid",
        "grid-template-columns: auto 800px auto",
        "margin:0px",
        "padding:0px"
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
        "p,h2,ul,ol,h1,pre", "grid-column-start : 2",
        "grid-column-end : 3",
        "width:inherit",
        "margin:15px"
    )
    css_file += util.addCss(
        "b,i,a", "grid-column-start : 2",
        "grid-column-end : 3",
        "padding-left:15px",
        "padding-right:15px"
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
        "max-width:500px",
        "border-radius: 10px 10px 0px 0px",
        "box-shadow: 1px 1px 12px grey;"
    )

    css_file += util.addCss(
        ".draggable_content",
        "max-height:400px",
        "overflow-y:auto",
    )

    css_file += util.addCss(
        ".ref_header",
        "cursor:move",
        "z-index:10",
        "background-color:#9c84a4",
        "color:#fff",
        "display: grid",
        "grid-template-columns: 10px auto 20px 10px",
        "grid-column-start: 1",
        "align-items: center",
        "border-radius: 10px 10px 0px 0px"
    )
    css_file += util.addCss(
        ".navbar",
        "background: white",
        "position: fixed",
        "top : 0px",
        "height:100%",
        "z-index:100",
        "-webkit-transition: all 0.3s ease",
        "-moz-transition: all 0.3s ease",
        "transition: all 0.3s ease"
    )
    css_file += util.addCss(
        ".navbar h3",
        "color: white",
        "font-size: 1.9em",
        "padding: 20px",
        "margin: 0",
        "font-weight: 300",
        "background: var(--primary)",
        "float:left"
    )
    css_file += util.addCss(
        ".navbar a",
        "display: block",
        "color: black",
        "font-size: 1.1em",
        "font-weight: 300"
    )
    css_file += util.addCss(
        ".navbar a:hover",
        "background: var(--highlight)",
        "color:white"
    )
    css_file += util.addCss(
        ".navbar a",
        "padding-top: 5px",
        "padding-bottom: 5px",
    )
    css_file += util.addCss(
        ".navbar a:link",
        "text-decoration:none"
    )
    css_file += util.addCss(
        ".dropdown-container",
        "display: none",
        "padding-left: 8px"
    )
    css_file += util.addCss(
        "#exitNavBar", "float:right",
        "cursor: pointer"
    )
    css_file += util.addCss(
        ".navButton",
        "position: fixed",
        "top:10px",
        "background-color: var(--primary)",
        "width: 75px",
        "height: 75px",
        "border-radius: 50px",
        "grid-column-start: 1",
        "box-shadow:2px 2px 8px 2px  darkgray",
        "cursor: pointer"
    )
    css_file += util.addCss(
        ".bar",
        "width: 35px",
        "height: 5px",
        "background-color: white",
        "margin: 6px 20px"
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
        "\tx_offset = e.clientX",
        "\ty_offset = e.clientY",
        "}\n"

        "function endDrag(e){",
        "\tlet obj = e.target.parentNode;",
        
        "\tlet x = x_offset - e.clientX;",
        "\tlet y = y_offset - e.clientY;",

        "\tobj.style.left = (obj.offsetLeft - x) + \"px\";",
        "\tobj.style.top = (obj.offsetTop - y) + \"px\";",
        "}\n\n",

        "function dragstart_handler(e) {",
        "\te.dataTransfer.setData(\"text/plain\", e.target.innerText);",
        "}"
        )

    js_file += util.constructString(
        "function moveToPosition(e, element){",
        "\tlet obj = document.getElementById(element);",
        "\tobj.style.left = e.pageX + 'px';",
        "\tobj.style.top = e.pageY + 'px';",
        "}"
    )
    js_file += util.constructString(
        "document.addEventListener('DOMContentLoaded', function() {",
        "\tmenuLeft = document.getElementById( 'navbar' );",
        "\tbody = document.body;",
        "\tshowLeft = document.getElementById( 'showLeft' );",
        "\tmenuLeft.style.left = \"-500px\";",
        "\tvar dropdown = document.getElementsByClassName(\"dropdown-btn\");",
        "\tvar i;",
        "\tfor (i = 0; i < dropdown.length; i++) {",
        "\t\tdropdown[i].addEventListener(\"click\", function() {",
        "\t\tthis.classList.toggle(\"active\");",
        "\t\tvar dropdownContent = this.nextElementSibling;",
        "\t\tdropdownContent.style.display = dropdownContent.style.display === \"none\" ? \"block\" : \"none\";"
        "\t\t});",
        "\t}",
        "});\n"
    )
    js_file += util.constructString(
        "function toggleNavBar(){",
        "\tmenuLeft.style.left = menuLeft.style.left == \"0px\" ? \"-500px\" : \"0px\";",
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

    #if the user gave a third param, make the book there
    if(len(sys.argv) == 3):
        os.chdir(sys.argv[2])

    #create directories for book if they don't exist
    if not os.path.exists(filename):
        os.mkdir(filename)

    os.chdir(filename)

    if not os.path.exists("media"):
        os.mkdir("media")

    html_fd = initFile(filename)

    parser.parse(html_fd, fd)


if __name__ == "__main__":
    main()