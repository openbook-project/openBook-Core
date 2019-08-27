import util
import htmlwriter
from collections import OrderedDict

keys = {'title' : htmlwriter.writeTitle,
        'par' : htmlwriter.writePar,
        'item': htmlwriter.listItem,
        'code': htmlwriter.addCode,
        'link': htmlwriter.addLink,
        'break': htmlwriter.addLine,
        'ref' : htmlwriter.linkRef,
        'img':htmlwriter.addImage,
        'subtitle': htmlwriter.addSubTitle,
        'pad' : htmlwriter.addPadding
        }

nestable = {'big' : htmlwriter.startBig,
            'big_end' : htmlwriter.endBig,
            'list' : htmlwriter.startList,
            'list_end' : htmlwriter.endList,
            'bold' : htmlwriter.startBold,
            'bold_end' : htmlwriter.endBold,
            'emph' : htmlwriter.startEmph,
            'emph_end' : htmlwriter.endEmph,
            'tex' : htmlwriter.startTex,
            'tex_end' : htmlwriter.endTex
            }

groups = {'ref' : htmlwriter.startRef,
          'ref_end':htmlwriter.endRef }

def write(html_file, tokens):
    stack = []
    group = []

    for t in tokens:
        tag = list(t.keys())[0]
        content = t[tag]
        options = t["options"]
        line = t["line"]

        if tag in keys and tag in groups:
            #determine which type we're dealing with
            if util.isSrcRef(options):
                option_keys = util.tokenizeOptions(options)
                html_file.write(groups[tag](content,option_keys, line))
                stack.append(tag)
            else:
                html_file.write(keys[tag](content,options,line))

        elif tag in keys:
            html_file.write(keys[tag](content, options, line))
        elif tag in nestable:
            html_file.write(nestable[tag](content, options, line))
            stack.append(tag)

        elif tag == "end":
            if len(stack) > 0:
                func = stack.pop() + "_end"
                if func in nestable:
                    html_file.write(nestable[func]())
        
                elif func in groups:
                    html_file.write(groups[func]())


    html_file.write( htmlwriter.buildNavBar() )
            

#first tokenize the file
def parse(html_file, source_file):
    ret = []

    buff = ""
    token = ""
    last_token = ""
    last_options = []
    outside_token = True
    prev_char = ""

    line_number = 0
    last_line = 0

    for line in source_file:
        line_number += 1
        for ch in line:
            if ch != '#' or (ch == '#' and prev_char == "\\"):
                if ch == '#' and prev_char == '\\':
                    buff = buff.replace("\\", "", 1)

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
                        tmp["line"] = last_line
                        ret.append( tmp  )
                    buff = ""
                #now going outside the token, save the token
                else:
                    token = token.strip("#")
                    token = token.strip()
                    r = util.parseOptions(token)

                    last_token = r[0]
                    last_token = last_token.lower()
                    last_options = r[1]
                    last_line = line_number
                    token = ""
                outside_token = not outside_token

            prev_char = ch

    #save whatever is left in the buffer
    if last_token != "" or buff != "":
        buff = buff.strip()
        tmp = OrderedDict()
        tmp[last_token] = buff
        tmp["options"] = last_options
        tmp["line"] = last_line
        ret.append( tmp )

    #write the tokenized version to the html file
    write(html_file, ret)

    


