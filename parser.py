import re
import os

KEYS = ['title', 'emph', 'bold','par', 'image', 'vid', 'code', 'list', 'item', 'end']
NESTABLE = ['emph', 'bold']
CONVERSION = {'title' : 'h1', 'emph' : 'i', 'bold' : 'b', 'par' : 'p', 'list' : 'ul', 'item' : 'li', 'code' : 'pre'}
media_path = os.getcwd() + "/media/"

title_count = 0

def parse(str):
	key = ''
	op = ''
	blocks = []
	data_params = []

	for c in str:
		# end a delimiter
		if c == '#' and '#' in key:
			op = re.sub('[#]', '', key)
			source = re.search('\[(.*?)\]', key)
			if source != None:
				data_params.append(source.group(1))	
				blocks.append(op.replace('[' + source.group(1) + ']', ''))
			else:
				blocks.append(op)
			key = ''
		
		# start a delimiter 
		elif c == '#':
			if newline_util(key) and op != '':
				blocks.append(key)
			key = ''
			key += c
		else:
			key += c
	blocks.append(key)
	blocks[:] = [x for x in blocks if x not in  ['', '\n']]
	return blocks[:-1], data_params

def driver(blocks, out_file, data = []):
	stack = []
	nested = False
	for content in blocks:
		if content in KEYS:
			# check for non content tags
			if content == 'list':
				html_list(content, out_file)
			elif content == 'image':
				html_image(content, "TMP", out_file)
			elif content == 'vid':
				html_image(content, "TMP", out_file)
			
			# handles implicit and explicit end
			elif stack and content == 'end':
				html_end(stack[0], out_file)
				stack.pop(0)
			elif stack and content not in NESTABLE:
				html_end(stack[0], out_file)
				stack.pop(0)
				stack = [content] + stack
			elif content in NESTABLE:
				stack = [content] + stack
				nested = True
			else:
				stack = [content] + stack

		else:
			# print(stack)
			func = stack[0]
			if func not in NESTABLE and nested:
				print('trigger: ' + str(nested))
				html_write(content, out_file) 
				nested = False
			elif func == 'title':
				html_title(content, out_file)
				stack.pop(0)
			elif func == 'par':
				html_par(content, out_file)
			elif func == 'code':
				html_code(content,out_file)
			elif func == 'item':
				html_item(content, out_file)
			elif func == 'bold':
				html_bold(content, out_file)
			elif func == 'emph':
				html_emph(content, out_file)
			else:
				print('Warning: ' + func + ' operation not found')	

def html_title(content, out_file):
	out_file.write('<h1>' + re.sub('[\n]', '', content) + '</h1>\n')

def html_par(content, out_file):
	out_file.write('<p>' + content)

def html_image(content, name, out_file):
	out_file.write('<img src="' + name + '">\n')

def html_vid(content, name, out_file):
	out_file.write('<video width = "250" controls><source src="' + media_path + 'videos/' + name + '" type="video/mp4"></video>]\n')

def html_list(content, out_file):
	out_file.write('<ul>\n')

def html_item(content, out_file):
	out_file.write('<li>' + content)

def html_bold(content, out_file):
	out_file.write('<b>' + content)

def html_emph(content, out_file):
	out_file.write('<i>' + content)

def html_end(content, out_file):
	out_file.write('</' + CONVERSION[content] + '>\n')

def html_write(content, out_file):
	out_file.write(content)

def newline_util(content):
	for c in content:
		if c.replace('\n', '').replace('\t','') != '':
			return True
	return False

def html_code(content,out_file):
	out_file.write('<pre class="prettyprint linenums">' + content)


if __name__ == '__main__':
	# filename = input("enter a .book file name  ==> ")
	# file = open(filename, "r").read()
	# data = re.sub('[\r]', '', file)
	# control, args = parse(data)
	print(str(newline_util('\n\t')))
