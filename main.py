import parser


HTML = ""

if __name__ == "__main__":
	filename = input("enter a .book file name  ==> ")
	file = open(filename, "r").read()
	file.replace("\n","")
	file.replace("\r","")

	output = open("output.html", "w")
	outcss = open("output.css", "w")

	init_html = "<!DOCTYPE html><html><head><link rel='stylesheet' href='output.css'></head><body>"
	init_css = "html{font-family: Arial, Helvetica, sans-serif;line-height: 1.5;}h1{margin: 0px;}.container{display: flex;flex-direction: column ;justify-content: center;align-items: center;}#content{max-width: 50%;}"
	end_html = "</body></html>"
	output.write(init_html)
	outcss.write(init_css)

	output.close()
	content = parser.parse(file)

	print(content)
	output = open('output.html', 'a')

	parser.driver(content, output)
	output.write(end_html)

	output.close()