from collections import OrderedDict

counter = {'title' : 0,
           'par' : 0,
           'item' : 0,
           'subtitle' : 0
          }

index_list = OrderedDict()

def recordTitle(index, name):
    index_list["title" + str(index)] = name

def recordSubtitle(index, name):
    index_list["subtitle" + str(index)] = name

