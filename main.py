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

	title_count = len(re.findall(".*#title#", file))
	navbar = "Chapter Select: <select onchange='jump_section()'id='chapter_select'>"
	for i in range(title_count):
		navbar += "<option value = 'chapter : " + str(i+1) + "'>" + str(i+1) + "</option>"

	navbar += "</select>"
	
	book_name = "<span style='padding-right:25px;'><b>" + filename + "</b></span>"

	init_html = "<!DOCTYPE html>\n<html>\n<head><title>" + filename + "</title>\n<script src='https://cdn.jsdelivr.net/gh/google/code-prettify@master/loader/run_prettify.js?skin=sunburst'>\n</script>\n<link rel='stylesheet' href='output.css'>\n</head>\n<body>\n<div id='navbar'>" + book_name + navbar + "</div><div class='container'>\n<div id='content'>"
	init_css = "html{font-family: Arial, Helvetica, sans-serif;line-height: 1.5;}\nh1,body{margin: 0px;padding:0 px;}\n.container{margin-top:65px;display: flex;flex-direction: column ;justify-content: center;align-items: center;}\n#content{max-width: 50%;}\n#navbar{position:fixed;width:100%;height:25px;top:0px;border-bottom:solid 1px black;padding:10px;background-color:white;}\n"

	c_select = "#chapter_select{}\n"
	drag_def = ".def{position:absolute;background-color:white;border:solid 1px black; padding-left:10px;padding-right : 10px;}"

	init_css += c_select + drag_def

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
	content, media = parser.parse(file)

	#print(content)
	# print(media)
	output = open('output.html', 'a')

	parser.driver(content, output, media)
	output.write(end_html)

	init_js = "<script>function jump_section(){var section = document.getElementById('chapter_select');var index = section.selectedIndex+1; window.location = '#title' + index;}"
	#drag_js = "dragElement(document.getElementById('def1'));function dragElement(elmnt) {var pos1 = 0, pos2 = 0, pos3 = 0, pos4 = 0;if (document.getElementById(elmnt.id + 'header')) {/* if present, the header is where you move the DIV from:*/document.getElementById(elmnt.id + 'header').onmousedown = dragMouseDown;} else { elmnt.onmousedown = dragMouseDown;}function dragMouseDown(e) { e = e || window.event;e.preventDefault();pos3 = e.clientX;pos4 = e.clientY;document.onmouseup = closeDragElement; document.onmousemove = elementDrag;}function elementDrag(e) {e = e || window.event;e.preventDefault();pos1 = pos3 - e.clientX;pos2 = pos4 - e.clientY;pos3 = e.clientX;pos4 = e.clientY;elmnt.style.top = (elmnt.offsetTop - pos2) + 'px';elmnt.style.left = (elmnt.offsetLeft - pos1) + 'px';}function closeDragElement() {document.onmouseup = null;document.onmousemove = null;}}"
	#hide_js = "function hideMe(id){var x = document.getElementById(id);if (x.style.display === 'none') {x.style.display = 'block';} else {x.style.display = 'none'; }}</script>"
	output.write(init_js)

	output.close()

	#fin_file = open('output.html', 'r+')
	#parser.post_process(fin_file.read(), "recursion", 1, fin_file)

	outcss.close()