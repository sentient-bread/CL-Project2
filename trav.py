from tree import *
from rules import *
import copy

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
        validfuncs = ['main','k1','k1s','k2','k2p','k3','rt','rh','k5','r6','k7p','k7t','pof']
        
        if getkar(change) in validfuncs:
            success = eval(getkar(change))(change)
        else:
            success = None
        
        if success:
            list.append(tree2)
        for child in const[1:]:
            getques(tree, child, list)
    
    list = []
    getques(tree, tree, list)
    return list
