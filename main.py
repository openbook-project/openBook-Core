import parser
import os
import re
import sys
import ntpath
import shutil

HTML = ""

def build_js():
	return '''
	<script>\nvar edits = [];
	var list = document.getElementsByClassName(\'edit\');
	for(var i = 0;i < list.length; i++){
		edits.push(CodeMirror(document.getElementById(list[i].id)));} 
		function getText(index){return edits[index].getValue();
	}
	function jump_section(){
		var section = document.getElementById('chapter_select');
		var index = section.selectedIndex+1; window.location = '#title' + index;
	}'''

'''
params js libs to add in head, filename, bookname, navbar
return html string
starts the output by writing the head and starting the content div
'''
def build_head(latex, code_mirror, filename, navbar):
	book_name = "<span style='padding-right:25px;'><b>" + filename + "</b></span>"
	init_html = "<!DOCTYPE html>\n<html>\n<head>\n" + latex  + "\n" + code_mirror 
	init_html += "<title>" + filename + "</title>\n\
	<script src='https://cdn.jsdelivr.net/gh/google/code-prettify@master/loader/run_prettify.js?skin=sunburst'>\n\
	</script>\n<link rel='stylesheet' href='" + filename + ".css'>\n"
	init_html +=  "<meta name='viewport' content='width=device-width, initial-scale=1.0'>\n\
	</head>\n<body>\n<div id='navbar'>" + book_name + navbar
	init_html += "</div><div class='container'>\n<div id='content'>"
	return init_html
	
'''
params  number of titles in the current file
returns html string
builds a navigation bar that allows jumping to different chapters
'''
def build_navbar(title_count):
	navbar = "\nChapter Select: <select onchange='jump_section()' id='chapter_select'>"
	for i in range(title_count):
		navbar += "<option value = 'chapter : " + str(i+1) + "'>" + str(i+1) + "</option>"

	navbar += "</select>"
	return navbar

if __name__ == "__main__":
	#get the location of the file to parse
	filename = ''
	if len(sys.argv) <= 1:
		filename = input("enter a .book file name  ==> ")
	else:
		filename = sys.argv[1]

	file = open(filename, "r").read()
	file.replace("\n","")
	file.replace("\r","")

	init_css = open("css_file.css").read()
	#get the name of the file from the path and remove the extension
	filename = ntpath.basename(filename)[:-5]

	#create a new folder for the output
	if not os.path.exists(filename):
		os.mkdir(filename)

	os.chdir(filename)

	#create output
	output = open(filename + ".html", "w")
	outcss = open(filename + ".css", "w")

	title_count = len(re.findall(".*#title#", file))
	navbar = build_navbar(title_count)

	#javascript scripts
	code_mirror = "<script src=\"../lib/codemirror.js\"></script><link rel=\"stylesheet\" href=\"../lib/codemirror.css\"><script src=\"../mode/javascript/javascript.js\"></script>"
	latex = '<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/latest.js?config=TeX-MML-AM_CHTML"></script>'
	latex_settings = '<script type="text/x-mathjax-config">MathJax.Hub.Config({tex2jax: {inlineMath: [[\'$$\',\'$$\'], [\'\\(\',\'\\)\']]}});</script>'

	init_html = build_head(latex, code_mirror, filename, navbar)

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

	init_js = build_js()
	output.write(init_js)

	output.close()
	outcss.close()
