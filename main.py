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

	init_html = "<!DOCTYPE html><html><head><link rel='stylesheet' href='output.css'></head><body>"
	output.write(init_html)
	parse(file)