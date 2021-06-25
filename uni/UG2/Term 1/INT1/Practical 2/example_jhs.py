# import the tree generation code and pretty-printer
from randomTree_jhs import *
import pprint_jhs

# changing this value will give you a different random tree:
tree_id = 4

# need to initialise our pretty-printer
p = pprint_jhs.PrettyPrinter(width=15)

# generate the tree
t = getTree(tree_id)

# print it out
p.pprint(t)

