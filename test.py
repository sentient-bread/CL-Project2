from __future__ import unicode_literals
from isc_parser import Parser
from trav import *

sentence = "नादिरशाह की सेना ने दिल्ली में कत्लेआम कर रखा है"
parser = Parser(lang='hin')
tree = parser.parse(sentence.split())
print(tree)
tree = maketree(tree)
ql = traverse(tree)
