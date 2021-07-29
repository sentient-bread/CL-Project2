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
    """
    Generates a list of questions for the whole tree.
    """
    def getques(tree, const, list):
        tree2 = copy.deepcopy(tree)
        for t in tree2:
            change = findrec(const[0].ind, t)
            if (change != None):
                break
                
        validfuncs = ['main','k1','k1s','k2','k2p','k3','rt','rh','k5','r6','k7p','k7t','pof', 'nmod__adj']
        
        if getkar(change) in validfuncs:
            success = eval(getkar(change))(change)
        else:
            success = None
        
        if success:
            list.append(tree2)
        for child in const[1:]:
            getques(tree, child, list)
    
    list = []
    for i, t in enumerate(tree):
        r = findkar('nmod__relc', t)
        if r != None:
            mahakarak('', r)
        if t[0].pos == 'VM':                        # if the root is a finite verb
            getques(tree, t, list)
        elif t[0].pos == 'CC' and len(t) >= 3:      # else if the root is conjunction
            tree1 = copy.deepcopy(tree)
            tree2 = copy.deepcopy(tree) # we need two copies as python uses references
            
            t1 = tree1[i]
            t2 = tree2[i]               # copies of t in tree1 and tree2
            
            t1[0].spel = ''
            mahakarak('',t1[2])
            getques(tree1, t1[1], list) # eliminating second clause and getting qs of first
            
            t2[0].spel = ''
            mahakarak('',t2[1])
            getques(tree2, t2[2], list) # eliminating first clause and getting qs of second
            
    return list
