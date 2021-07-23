from tree import *
from rules import *
import copy

tree = maketree(sentence)

def emp(const):
    const[0].spel = ''
    for child in const[1:]:
        emp(child)

def findrec(index, tree):
    if index == tree[0].ind:
        return tree
    else:
        for child in tree[1:]:
            f = findrec(index, child)
            if f != None:
                return f
        return None

def traverse(tree):
    def getques(tree, const, list):
        tree2 = copy.deepcopy(tree)
        change = findrec(const[0].ind, tree2)
        
        success = eval(getkar(change))(change)
        
        if success:
            list.append(tree2)
        for child in const[1:]:
            getques(tree, child, list)
    
    list = []
    getques(tree, tree, list)
    return list
