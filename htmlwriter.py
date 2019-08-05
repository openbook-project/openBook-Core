
# given a tag creates a properlly 
# formatted string 
# e.g p, content => <p> content </p>
def writeHTMLTag(tag, content):
	ret = "" 

	ret += "<" + tag + ">\n"
	ret += "\t" + content + "\n"
	ret += "</" + tag + ">\n"

	return ret

def writeTitle(content):
	ret = ""

	ret += "<h1>"
	ret += "\t" + content + "\n"
	ret += "</h1>\n"

	return ret

def writePar(content):
	ret = ""

	ret += "<p>\n"
	ret += "\t" + content + "\n"
	ret += "</p>\n"

	return ret

def startBig(content):
	ret = ""
	ret += "\t<h2>" + content

	return ret

def endBig():
	ret = "\t</h2>\n"
	return ret

def startList(content = ""):
	ret = ""	
	ret += "<ul>\n"

	return ret

def endList():
	ret = "</ul>\n"

	return ret

def listItem(content):
	return "\t<li>" + content + "</li>\n"