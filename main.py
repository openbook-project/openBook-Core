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

	init_html = "<!DOCTYPE html><html><head><link rel='stylesheet' href='output.css'></head><body><div class='container'><div id='content'>\n"
	init_css = "html{font-family: Arial, Helvetica, sans-serif;line-height: 1.5;}h1{margin: 0px;}.container{display: flex;flex-direction: column ;justify-content: center;align-items: center;}#content{max-width: 50%;}"
	end_html = "</div></div></body></html>"
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

	print(content[0])
	output = open('output.html', 'a')

	parser.driver(content[0], output)
	output.write(end_html)

	output.close()