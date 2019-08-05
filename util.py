
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