class Word:
    def __init__(self,ind, spel, pos, kar):
        self.ind = ind
        self.spel = spel
        self.pos = pos
        self.kar = kar
    
    def __str__(self):
        return str(self.spel)
    
    def __repr__(self):
        return str(self.spel)

def makeword(listitem):
    word = Word(listitem[0], listitem[1], listitem[3], listitem[7])
    return word

def subtree(word, pars):
    sub = [makeword(word)]
    sub += [subtree(child,pars) for child in pars if child[6] == word[0]]
    return sub

def maketree(pars):
    root = [word for word in pars if int(word[6]) == 0][0] # { word | word \in pars, word[6] == 0}
    tree = subtree(root,pars)
    return tree

def getkar(const):
    return const[0].kar
    
def makesent(tree):
    def getsent(tree, sent):
        sent[int(tree[0].ind)] = tree[0].spel
        for dep in tree[1:]:
            getsent(dep, sent)
        return sent

    sent = getsent(tree, {})
    
    sentence = []
    for i in range(len(sent)):
        if sent[i+1] != '':
            sentence.append(sent[i+1])
    return sentence
