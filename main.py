import parser
import os

HTML = ""

if __name__ == "__main__":
	filename = input("enter a .book file name  ==> ")
	file = open(filename, "r").read()
	file.replace("\n","")
	file.replace("\r","")

	output = open("output.html", "w")
	outcss = open("output.css", "w")

	init_html = "<!DOCTYPE html>\n<html>\n<head>\n<script src='https://cdn.jsdelivr.net/gh/google/code-prettify@master/loader/run_prettify.js?skin=sunburst'>\n</script>\n<link rel='stylesheet' href='output.css'>\n</head>\n<body>\n<div class='container'>\n<div id='content'>"
	init_css = "html{font-family: Arial, Helvetica, sans-serif;line-height: 1.5;}\nh1{margin: 0px;}\n.container{display: flex;flex-direction: column ;justify-content: center;align-items: center;}\n#content{max-width: 50%;}"
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

	output = open('output.html', 'a')

	parser.driver(content[0], output)
	output.write(end_html)

	init_js = "<script></script>"
	output.write(init_js)

	output.close()