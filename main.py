import parser
import os
import re

HTML = ""

if __name__ == "__main__":
	filename = input("enter a .book file name  ==> ")
	file = open(filename, "r").read()
	file.replace("\n","")
	file.replace("\r","")

	output = open("output.html", "w")
	outcss = open("output.css", "w")

	title_count = len(re.findall("^.*#title#", file))
	navbar = "Chapter Select: <select id='chapter_select'>"
	for i in range(title_count):
		navbar += "<option value = 'chapter : " + str(i+1) + "'>" + str(i+1) + "</option>"

	navbar += "</select>"
	
	book_name = "<span style='padding-right:25px;'><b>" + filename + "</b></span>"

	init_html = "<!DOCTYPE html>\n<html>\n<head><title>" + filename + "</title>\n<script src='https://cdn.jsdelivr.net/gh/google/code-prettify@master/loader/run_prettify.js?skin=sunburst'>\n</script>\n<link rel='stylesheet' href='output.css'>\n</head>\n<body>\n<div id='navbar'>" + book_name + navbar + "</div><div class='container'>\n<div id='content'>"
	init_css = "html{font-family: Arial, Helvetica, sans-serif;line-height: 1.5;}\nh1,body{margin: 0px;padding:0 px;}\n.container{margin-top:65px;display: flex;flex-direction: column ;justify-content: center;align-items: center;}\n#content{max-width: 50%;}\n#navbar{position:fixed;width:100%;height:25px;top:0px;border-bottom:solid 1px black;padding:10px;background-color:white;}\n"

	c_select = "#chapter_select{}\n"

	init_css += c_select

	end_html = "</div>\n</div>\n</body>\n</html>"

	output.write(init_html)
	outcss.write(init_css)

	#create a media folder if one doesn't exist
	path = os.getcwd() + "/media"
	if not(os.path.exists(path)):
		os.mkdir(path)
		os.mkdir(path + "/images")
		os.mkdir(path + "/videos")

	output.close()
	content = parser.parse(file)

	# print(content[0])
	output = open('output.html', 'a')

	parser.driver(content[0], output)
	output.write(end_html)

	init_js = "<script></script>"
	output.write(init_js)

	output.close()