def main():
	print("Hello world")

def parse(file):
	print(file)

if __name__ == "__main__":
	filename = input("enter a .book file name  ==> ")
	file = open(filename, "r").read()
	file.replace("\n","")
	file.replace("\r","")

	parse(file)