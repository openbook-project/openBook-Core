import util
import htmlwriter

keys = {'title' : htmlwriter.writeTitle,
		'par' : htmlwriter.writePar,
		'item': htmlwriter.listItem
		}

nestable = {'big' : htmlwriter.startBig,
			'big_end' : htmlwriter.endBig,
			'list' : htmlwriter.startList,
			'end_list' : htmlwriter.endList
			}

def write(html_file, tokens):
	stack = []
	for t in tokens:
		tag = list(t.keys())[0]
		content = t[tag]
		if tag in keys:
			html_file.write(keys[tag](content))
		elif tag in nestable:
			html_file.write(nestable[tag](content))
			stack.append(tag)
		elif tag == "end":
			if len(stack) > 0:
				func = stack.pop() + "_end"
				if func in nestable:
					html_file.write(nestable[func]())
			

#first tokenize the file
def parse(html_file, source_file):
	ret = []

	buff = ""
	token = ""
	last_token = ""
	outside_token = True
	prev_char = ""

	for line in source_file:
		for ch in line:
			if ch == '\n' or ch == '\r':
				continue

			if ch != '#' or (ch == '#' and prev_char == "\\"):
				if not outside_token:
					token += ch
				else:
					buff += ch

			if ch == '#' and prev_char != "\\":
				#now going inside the token, add the buffer to the last token
				if outside_token:
					if buff != "" or last_token != "":
						buff = buff.strip()
						ret.append({last_token : buff})
					buff = ""
				#now going outside the token, save the token
				else:
					last_token = token
					last_token = last_token.strip('#')
					last_token = last_token.strip()
					token = ""
				outside_token = not outside_token

			prev_char = ch


	#save whatever is left in the buffer
	if last_token != "" or buff != "":
		buff = buff.strip()
		ret.append({last_token : buff})

	# for x in ret:
	# 	print(x)

	#write the tokenized version to the html file
	write(html_file, ret)

	


