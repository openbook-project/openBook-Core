import parser
import os
import re
import sys
import ntpath

HTML = ""

if __name__ == "__main__":

	filename = ''
	if len(sys.argv) <= 1:
		filename = input("enter a .book file name  ==> ")
	else:
		filename = sys.argv[1]

	file = open(filename, "r").read()
	file.replace("\n","")
	file.replace("\r","")

	filename = ntpath.basename(filename)

	output = open(filename + ".html", "w")
	outcss = open(filename + ".css", "w")

	title_count = len(re.findall(".*#title#", file))
	navbar = "Chapter Select: <select onchange='jump_section()'id='chapter_select'>"
	for i in range(title_count):
		navbar += "<option value = 'chapter : " + str(i+1) + "'>" + str(i+1) + "</option>"

	navbar += "</select>"
	book_name = "<span style='padding-right:25px;'><b>" + filename + "</b></span>"

	#javascript scripts
	code_mirror = "<script src=\"lib/codemirror.js\"></script><link rel=\"stylesheet\" href=\"lib/codemirror.css\"><script src=\"mode/javascript/javascript.js\"></script>"
	latex = '<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/latest.js?config=TeX-MML-AM_CHTML"></script>'
	latex_settings = '<script type="text/x-mathjax-config">MathJax.Hub.Config({tex2jax: {inlineMath: [[\'$$\',\'$$\'], [\'\\(\',\'\\)\']]}});</script>'

	init_html = "<!DOCTYPE html>\n<html>\n<head>" + latex  + code_mirror + "<title>" + filename + "</title>\n<script src='https://cdn.jsdelivr.net/gh/google/code-prettify@master/loader/run_prettify.js?skin=sunburst'>\n</script>\n<link rel='stylesheet' href='" + filename + ".css'>\n</head>\n<body>\n<div id='navbar'>" + book_name + navbar + "</div><div class='container'>\n<div id='content'>"
	init_css = open("css_file.css").read()

	end_html = "<br><br><br></div>\n</div>\n</body>\n</html>"

	output.write(init_html)
	outcss.write(init_css)

	#create a media folder if one doesn't exist
	path = os.getcwd() + "/media"
	if not(os.path.exists(path)):
		os.mkdir(path)
		os.mkdir(path + "/images")
		os.mkdir(path + "/videos")

	output.close()
	content, media = parser.parse(file)

	output = open(filename + '.html', 'a')

	parser.driver(content, output, media)
	output.write(end_html)

	init_js = "<script>var edits = [];var list = document.getElementsByClassName(\'edit\');for(var i = 0;i < list.length; i++){edits.push(CodeMirror(document.getElementById(list[i].id)));} function getText(index){return edits[index].getValue();} function jump_section(){var section = document.getElementById('chapter_select');var index = section.selectedIndex+1; window.location = '#title' + index;}"
	downloadjs = "function download(filename, text) {var element = document.createElement('a');element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(text));element.setAttribute('download', filename);element.style.display = 'none';document.body.appendChild(element);element.click();document.body.removeChild(element);}</script>"
	
	output.write(init_js + downloadjs)

	output.close()
	outcss.close()