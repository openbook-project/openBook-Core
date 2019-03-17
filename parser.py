import re
import os

KEYS = ['title', 'emph', 'bold','par', 'image', 'vid', 'code', 'list', 'item', 'end', 'big', 'def']
NESTABLE = ['emph', 'bold', 'list', 'code']
CONVERSION = {'title' : 'h1', 'emph' : 'i', 'bold' : 'b', 'big': 'h2','par' : 'p', 'list' : 'ul', 'item' : 'li', 'code' : 'pre', 'def' : 'div'}
media_path = "media/"

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
	title_count = def_count = 0
	nested = False
	for content in blocks:
		if content in KEYS:
			# handles implicit and explicit end
			if stack and content == 'end':
				# print('ending op: ' + stack[0])
				if stack[0] == 'item' and stack[1] == 'list':
					html_end(stack[0], out_file)
					stack.pop(0)
				html_end(stack[0], out_file)
				stack.pop(0)
			elif content == 'list':
				if stack:
					nested = False
					html_end(stack[0], out_file)
					stack.pop(0)
				html_list(content, out_file)
				stack = [content] + stack
			elif stack and content not in NESTABLE and stack[0] not in NESTABLE:
				html_end(stack[0], out_file)
				stack.pop(0)
				stack = [content] + stack
			elif content in NESTABLE:
				stack = [content] + stack
				nested = True

			# check for non content tags
			elif content == 'image':
				html_image(content, data[0], out_file)
				data.pop(0)
			elif content == 'vid':
				html_image(content, "TMP", out_file)

			# base case
			else:
				stack = [content] + stack

		else:
			#print(stack)
			func = stack[0]
			if func not in NESTABLE and nested:
				html_write(content, out_file) 
				nested = False
			elif func == 'title':
				title_count += 1
				html_title(content, out_file, title_count)
				stack.pop(0)
			elif func == 'par':
				html_par(content, out_file)
			elif func == 'code':
				html_code(content,out_file)
			elif func == 'item':
				html_item(content, out_file)
			elif func == 'bold':
				html_bold(content, out_file)
			elif func == 'big':
				html_big(content, out_file)
			elif func == 'emph':
				html_emph(content, out_file)
			elif func == 'def':
				def_count += 1
				html_def(content,data[0], def_count, out_file)
			else:
				print('Warning: ' + func + ' operation not found')	

def html_title(content, out_file, id_ = 0):
	out_file.write('<h1 id = "title' + str(id_) +'">' + re.sub('[\n]', '', content) + '</h1>\n')

def html_par(content, out_file):
	out_file.write('<p>' + content)

def html_image(content, name, out_file):
	out_file.write('<img src="' "media/images/" + name + '">\n')

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

def html_big(content, out_file):
	out_file.write('<h2>' + content)

def html_end(content, out_file):
	out_file.write('</' + CONVERSION[content] + '>\n')

def html_write(content, out_file):
	out_file.write(content)

def html_def(content, data, count, out_file):
	out_file.write('<div class="def" id="def' + str(count) + '"><div id="def' + str(count) + 'header"><h2>' + data + '</h2></div><p>' + content + '</p>')

def newline_util(content):
	for c in content:
		if c.replace('\n', '').replace('\t','') != '':
			return True
	return False

def html_code(content,out_file):
	leading = re.match(r"\s*", content).group()
	out_file.write('<pre class="prettyprint linenums">' + content.replace(leading,'\n'))

def post_process(file, def_string, def_index, out_file):
	file = file.replace(def_string, "<a href='#' onclick='hideMe(\"def" + str(def_index) + "\"); return false;'> " + def_string + "</a>")
	name = out_file.name
	out_file.close()
	out_file = open(name, "w")
	out_file.write(file)


if __name__ == '__main__':
	# filename = input("enter a .book file name  ==> ")
	# file = open(filename, "r").read()
	# data = re.sub('[\r]', '', file)
	# control, args = parse(data)
	print(str(newline_util('\n\t')))
