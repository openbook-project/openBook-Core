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
	for content in blocks:
		if content in KEYS:
			# print(op)
			stack.append(content)
		else:
			func = stack.pop() 
			if func == 'title':
				html_title(content, out_file)
			elif func == 'par':
				html_par(content, out_file)
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

def html_title(content, out_file):
	out_file.write('<h1>' + re.sub('[\n]', '', content) + '</h1>')

def html_par(content, out_file):
	out_file.write('<p>' + content + '</p>')

if __name__ == '__main__':
	filename = input("enter a .book file name  ==> ")
	file = open(filename, "r").read()
	# file.replace('\n','')
	# file.replace('\r','')
	data = re.sub('[\r]', '', file)
	control = parse(data)
	drive(control)
