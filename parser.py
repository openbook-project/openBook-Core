import re

KEYS = ['title', 'emph', 'bold','par', 'image', 'vid', 'code', 'list', 'item', 'end']

def parse(str):
	key = ''
	op = ''
	blocks = []

	for c in str:
		# end a delimiter
		if c == '#' and '#' in key:
			op = re.sub('[#]', '', key)
			blocks.append(op)
			key = ''
		
		# start a delimiter 
		elif c == '#':
			if key != '' and op != '':
				blocks.append(key)
			key = ''
			key += c
		else:
			key += c
	return blocks

def driver(blocks, out_file):
	stack = []
	for op in blocks:
		if op in KEYS:
			print(op)
			stack.append(op)
		else:
			func = stack.pop() 
			if func == 'title':
				title(op, out_file)
			elif func == 'par':
				pass
			elif func == 'image':
				pass
			elif func == 'vid':
				pass
			elif func == 'code':
				pass
			elif func == 'list':
				pass
			elif func == 'item':
				pass
			elif func == 'end':
				pass
			else:
				print('Warning, operation not found')	

def title(content, out_file):
	out_file.write('<title>' + content + '</title>')

if __name__ == '__main__':
	filename = input("enter a .book file name  ==> ")
	file = open(filename, "r").read()
	# file.replace('\n','')
	# file.replace('\r','')
	data = re.sub('[\r]', '', file)
	control = parse(data)
	drive(control)
