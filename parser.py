import re

KEYS = ['title', 'par', 'image', 'vid', 'code', 'list', 'item', 'end']

def parse(str):
	key = ''
	op = ''
	blocks = []

	for c in str:
		# end a delimiter
		if c == '#' and '#' in key:
			op = re.sub('[#]', '', key)
			blocks.append(op)
			print(op)
			key = ''
		
		# start a delimiter 
		elif c == '#':
			if key != '' and op != '':
				blocks.append(key)
			key = ''
			key += c
		else:
			key += c
	print(blocks) 


if __name__ == '__main__':
	filename = input("enter a .book file name  ==> ")
	file = open(filename, "r").read()
	# file.replace('\n','')
	# file.replace('\r','')
	data = re.sub('[\r]', '', file)
	print(data)
	parse(data)
