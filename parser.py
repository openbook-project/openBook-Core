import re
import os

KEYS = ['title', 'emph', 'bold','par', 'image', 'vid', 'code', 'list', 'item', 'end']
media_path = os.getcwd() + "/media/"

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
	blocks.append(key)
	return blocks, data_params

def driver(blocks, out_file, data = []):
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
				html_image(content, "TMP", out_file)
			elif func == 'vid':
				html_vid(content, "TMP", out_file)
			elif func == 'code':
				html_code(content,out_file)
			elif func == 'list':
				pass
			elif func == 'item':
				pass
			elif func == 'end':
				pass
			else:
				print('Warning, ' + func + ' operation not found')	

def html_title(content, out_file):
	out_file.write('<h1>' + re.sub('[\n]', '', content) + '</h1>\n')

def html_par(content, out_file):
	out_file.write('<p>' + content + '</p>\n')

def html_image(content, name, out_file):
	out_file.write('<img src="' + name + '">\n')

def html_vid(content, name, out_file):
	out_file.write('<video width = "250" controls><source src="' + media_path + 'videos/' + name + '" type="video/mp4"></video>]\n')

def html_code(content,out_file):
	out_file.write('<pre class="prettyprint linenums">' + content + '</pre>')

if __name__ == '__main__':
	filename = input("enter a .book file name  ==> ")
	file = open(filename, "r").read()
	# file.replace('\n','')
	# file.replace('\r','')
	data = re.sub('[\r]', '', file)
	control = parse(data)
	#print(control)
	# driver(control)
