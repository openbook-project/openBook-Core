HTML = ""
def main():
	print("Hello world")

def parse(file):
	print(file)

if __name__ == "__main__":
	filename = input("enter a .book file name  ==> ")
	file = open(filename, "r").read()
	file.replace("\n","")
	file.replace("\r","")

	output = open("output.html", "w")
	outcss = open("output.css", "w")

	init_html = "<!DOCTYPE html><html><head><link rel='stylesheet' href='output.css'></head><body></html>"
	intit_css = "html{font-family: Arial, Helvetica, sans-serif;line-height: 1.5;}h1{margin: 0px;}.container{display: flex;flex-direction: column ;justify-content: center;align-items: center;}#content{max-width: 50%;}"

	output.write(init_html)
	outcss.write(init_css)
	parse(file)