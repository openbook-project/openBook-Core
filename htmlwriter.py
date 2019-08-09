

align_ops = {'center' : 'justify-self : center;',
			 'left' : 'justify-self : start;',
			 'right' : 'justify-self : end'}

counter = {'title' : 0,
		   'par' : 0,
		   'item' : 0}

#given a list of options searches if 
#any are of type style and returns a
#a list, val 1 is the number of styles
#found, val 2 is the acutal string
def getStyleOps(options):
	ret = []
	string = "style=\""
	count = 0

	for op in options:
		if op in align_ops:
			string += align_ops[op]
			count += 1

	string += "\""
	return [count, string]

def buildStyleString(*ops):
	ret = "style = \""
	for i in range(len(ops)):
		ret += ops[i] + ";"

	ret += "\""
	return ret

def buildId(tag):
	return "id=\"" + tag + str(counter[tag]) + "\""

# given a tag creates a properlly 
# formatted string 
# e.g p, content => <p> content </p>
def constructHTML(tag, content, style = "", end = True, args = []):
	ret = "" 

	ret += "<" + tag

	for i in range(len(args)):
		ret += " " + args[i]

	if style != "":
		ret += " " + style

	ret += ">"
	ret += "\t" + content + "\n"

	if end == True:
		ret += "</" + tag + ">\n"

	return ret

#construct a title
def writeTitle(content, ops = []):
	style = getStyleOps(ops)

	counter['title'] += 1
	ret = ""

	ret += "<h1 " + buildId('title') 
	if style[0] > 0:
		ret += " " + style[1] + ">"
	else:
		#by default a title is center aligned
		ret += " " + buildStyleString(align_ops['center']) + ">"

	ret += "\t" + content + "\n"
	ret += "</h1>\n"

	return ret

def writePar(content, ops = []):
	ret = ""

	ret += "<p>\n"
	ret += "\t" + content + "\n"
	ret += "</p>\n"

	return ret

#options |linenums -> enable line numbers
#	     |lang     -> target a specific language syntax 
def addCode(content, ops = []):
	ret = ""

	ln = ""
	if "linenums" in ops:
		ln = "linenums"

	ret = "<pre class = \"prettyprint" + ln + "\">\n"
	ret += "\t" + content + "\n"
	ret += "</pre>\n"

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

def listItem(content, ops = []):
	return "\t<li>" + content + "</li>\n"

def startBold(content):
	ret = ""
	ret += "<b>" + content

	return ret

def endBold():
	ret = "</b>\n"
	return ret

def startEmph(content):
	ret = ""
	ret += "<i>" + content

	return ret

def endEmph():
	ret = "</i>\n"
	return ret

#if ops is empty just past the entire link
#otherwise use an alternate
def addLink(content, ops=[]):
	alt = ""
	style = getStyleOps(ops)
	if len(style) > 0:
		style = style[1]

	if ops == []:
		alt = content
	else:
		for x in ops:
			x = x.strip()
			if "alt=" in x:
				alt = x.strip("alt=")
				break

	fields = ["href = \"" + content + "\""]
	ret = constructHTML("a", alt, style, True, fields)
	return ret

def startTex(content, ops=[]):
	ret = "<div>" + content
	return ret

def endTex():
	ret = "</div>\n"
	return ret