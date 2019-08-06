
# given a number of strings return
# them stitched together with a newline 
# between every string
def constructString(*arg):
	ret = ""
	for i in range(len(arg)):
		ret += arg[i] + "\n"

	return ret;

#given a head_name constructs a valid
#css string e.g:
# addCss('body', 'color:white', 'foo:ex' )
# willl return :
# body{
#	color:white;
#	foo:ex;
# }
def addCss(head_name, *objects):
	ret = head_name + "{\n"
	for i in range(len(objects)):
		ret += "\t" + objects[i] + ";\n"

	ret += "}\n"
	return ret

def addMediaQuery(min_size, max_size, head_name, *objects):
	ret = "@media only screen and (min-width: " + min_size + "px)"
	ret += " and (max-width: " + max_size +"px){\n"
	string = addCss(head_name, *objects).split("\n")
	for i in range(len(string)):
		# if i != 0:
		# 	ret += "\t"
		ret += "\t" + string[i] + "\n"

	ret += "}\n"
	return ret

def addJs(source):
	ret = "<script src = \"" + source + "\"></script>"
	return ret

#given a token (of type string) parses
#and returns any options, if none are
#entered an empty array is returned
#e.g: #foo |a,b ,c# will return:
#[foo,[a,b,c]]
def parseOptions(string):
	begin_search = False
	ret = []
	buff = ""
	token = ""
	for ch in string:
		if ch == "|":
			token = buff
			begin_search = True
			buff = ""
			continue

		if ch == ",":
			buff = buff.strip()
			ret.append(buff)
			buff = ""
			continue

		buff += ch

	#if there were no options just return the token
	if begin_search == False:
		token = buff
	elif buff != "":
		#save whatever is left in the buffer
		buff = buff.strip()
		ret.append(buff)

	token = token.strip()

	return [token, ret]