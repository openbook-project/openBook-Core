import util
import htmlwriter
from collections import OrderedDict

keys = {'title' : htmlwriter.writeTitle,
		'par' : htmlwriter.writePar,
		'item': htmlwriter.listItem,
		'code': htmlwriter.addCode,
		'link': htmlwriter.addLink
		}

nestable = {'big' : htmlwriter.startBig,
			'big_end' : htmlwriter.endBig,
			'list' : htmlwriter.startList,
			'list_end' : htmlwriter.endList,
			'bold' : htmlwriter.startBold,
			'bold_end' : htmlwriter.endBold,
			'emph' : htmlwriter.startEmph,
			'emph_end' : htmlwriter.endEmph
			}

def write(html_file, tokens):
	stack = []
	for t in tokens:
		tag = list(t.keys())[0]
		content = t[tag]
		options = t["options"]
		if tag in keys:
			html_file.write(keys[tag](content, options))
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
	last_options = []
	outside_token = True
	prev_char = ""

	for line in source_file:
		for ch in line:
			if ch != '#' or (ch == '#' and prev_char == "\\"):
				if outside_token:
					buff += ch
				else:
					token += ch

			if ch == '#' and prev_char != "\\":
				#now going inside the token, add the buffer to the last token
				if outside_token:
					if buff != "" or last_token != "":
						buff = buff.strip()
						# the token must always be first - use an ordered dict
						tmp = OrderedDict()
						tmp[last_token] = buff
						tmp["options"] = last_options
						ret.append( tmp  )
					buff = ""
				#now going outside the token, save the token
				else:
					token = token.strip("#")
					token = token.strip()
					r = util.parseOptions(token)

					last_token = r[0]
					last_options = r[1]
					token = ""
				outside_token = not outside_token

			prev_char = ch


	#save whatever is left in the buffer
	if last_token != "" or buff != "":
		buff = buff.strip()
		tmp = OrderedDict()
		tmp[last_token] = buff
		tmp["options"] = last_options
		ret.append( tmp )

	# for x in ret:
	# 	print(x)

	#write the tokenized version to the html file
	write(html_file, ret)

	


