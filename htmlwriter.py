import util
import os
import glob

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
    style = getStyleOps(ops)[1]

    ret = constructHTML("p", content, style )
    return ret

#options |linenums -> enable line numbers
#        |lang     -> target a specific language syntax 
def addCode(content, ops = []):
    ret = ""

    ln = ""
    if "linenums" in ops:
        ln = "linenums"

    ret = "<pre class = \"prettyprint" + ln + "\">\n"
    ret += "\t" + content + "\n"
    ret += "</pre>\n"

    return ret

def startBig(content, ops=[]):
    style = getStyleOps(ops)
    if len(style) > 0:
        style = style[1]
    else:
        style = ""

    ret = constructHTML("h2", content, style, True)

    return ret

def endBig():
    ret = "\t</h2>\n"
    return ret

def startList(content = "", ops=[]):
    ret = ""    
    ret += "<ul>\n"

    return ret

def endList():
    ret = "</ul>\n"

    return ret

def listItem(content, ops = []):
    return "\t<li>" + content + "</li>\n"

def startBold(content, ops=[]):
    ret = ""
    ret += "<b>" + content

    return ret

def endBold():
    ret = "</b>\n"
    return ret

def startEmph(content, ops=[]):
    style = getStyleOps(ops)[1]
    ret = constructHTML("i", content, style, False )

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
        key_ops = util.tokenizeOptions(ops)
        for x in key_ops:
            if "alt" in x:
                alt = x["alt"]
                break

    fields = ["href = \"" + content + "\"",
              "alt = \"" + alt + "\"" ,
              "target = \"_blank\""]
    ret = constructHTML("a", content, style, True, fields)
    return ret

def startTex(content, ops=[]):
    style = buildStyleString("max-width:100vw")
    ret = constructHTML("div", content, style, False )
    return ret

def endTex():
    ret = "</div>\n"
    return ret

def endRef():
    ret = "</div>"
    return ret

#content is ignored
def addLine(content, ops = []):
    styles = getStyleOps(ops)
    if styles[0] > 0:
        styles = styles[1]
    else:
        styles = buildStyleString('justify-self:center')

    ret = constructHTML('hr/', "", styles, False ) 
    return ret

def linkRef(content, ops=[]):

    key_ops = util.tokenizeOptions(ops)

    src = ""
    found = False
    for x in key_ops:
        if "src" in x:
            src = x["src"]
            found = True
            break

    link = "href=\"#" + src + "\""

    target = "\"" + src + "\""
    action = "onclick='moveToPosition(event, " + target + ") ; toggle(" + target + ");'"
    return constructHTML("a", src, "", True, [action,link])

def endRef():
    return "\t</div>\n</div>\n"

def startRef(content, ops=[]):
    name = ""
    for op in ops:
        if 'name' in op:
            name = op['name']
            break


    ret = constructHTML("div", "", "", False, 
        [
            'id="' + name + '"',
            'class="draggable"',
            'style="display:none;"'
        ] )
    ret += "\t"
    ret += constructHTML("div", "", "", False, 
        [ 
            'draggable="true"', 'class="ref_header"',
            'draggable="true"', 'ondragstart="beginDrag(event);',
            'dragstart_handler(event);"', 'ondragend = "endDrag(event)"'
        ] )

    ret += constructHTML("h2", name, "style='color:white;'")

    ret += constructHTML("div", "X", "style='justify-self:right; cursor:pointer; z-index:12;'", True, 
        ["onclick=\"this.parentNode.parentNode.style.display = 'none'\""] )

    ret += "\t</div>\n"
    ret += "<div class = 'draggable_content'>\n"

    return ret

def addImage(content, ops=[]):

    style = getStyleOps(ops)[1]

    #is this external or internal?
    key_ops = util.tokenizeOptions(ops)
    found = False
    alt = ""
    for x in key_ops:
        if "src" in x:
            src = x["src"]
            found = True
            break

    for x in key_ops:
        if "alt" in x:
            alt = x["alt"]
            break

    if not found:
        return ""

    external = util.isURL(src)
    
    #if we're an external image just copy the url in
    if alt == "":
        if external :
            alt = "external image"
        else :
            alt = src

    #otherwise we have to look for the name,
    #if there is no extension and its not an absolute path
    found = False
    src
    if not external:

        location = "media/"
        if os.path.isabs(src):
            location = src

        #do we have an extension
        if not util.isValidExtension(src):
            for file in os.listdir(location):
                filename = os.path.splitext(file)[0]

                if filename == src:
                    src = file
                    found = True
                    break

            #did not find the file, display err and return
            if not found:
                print("Warning : could not find file with base name of \"" + src + "\" under " + location)
                return ""
        src = "media/" + src



    ret = constructHTML("img", "", style, False, 
        ["src = \"" + src + "\"",
         "alt = \"" + alt + "\""
        ])

    return ret

def addSubTitle(content, ops=[]):
    style = getStyleOps(ops)[1]
    ret = constructHTML("h2", content, style, )
    return ret

def addPadding(content, ops=[]):
    return "</br>"
