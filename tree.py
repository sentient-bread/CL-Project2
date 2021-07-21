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
        sent[tree[0].ind] = tree[0].spel
        for dep in tree[1:]:
            sent.update(getsent(dep, sent))
        return sent

    sent = getsent(tree, {})
    
    sentence = []
    for i in range(len(sent)):
        sentence.append(sent[i+1])
    return sentence

sentence = [['1', 'उसका', 'उसका', 'PRP', 'PRP', '_', '2', 'r6', '_', '_'],
            ['2', 'विद्यारम्भ-संस्कार', 'विद्यारम्भ-संस्कार', 'NN', 'NN', '_', '7', 'k2', '_', '_'],
            ['3', 'भी', 'भी', 'RP', 'RP', '_', '2', 'lwg__rp', '_', '_'],
            ['4', 'खूब', 'खूब', 'QF', 'QF', '_', '5', 'nmod__adj', '_', '_'],
            ['5', 'धूम-धाम', 'धूम-धाम', 'NN', 'NN', '_', '7', 'adv', '_', '_'],
            ['6', 'से', 'से', 'PSP', 'PSP', '_', '5', 'lwg__psp', '_', '_'],
            ['7', 'किया', 'किया', 'VM', 'VM', '_', '0', 'main', '_', '_'],
            ['8', 'गया।', 'गया।', 'VAUX', 'VAUX', '_', '7', 'lwg__vaux', '_', '_']]
"""
[[1, 'यदि',   'यदि',    'CC',  'CC',  '_',9,'vmod','_','_'],
            [2, 'आप',   'आप',    'PRP', 'PRP', '_',7,'k1','_','_'],
            [3, 'इस',    'इस',    'DEM', 'DEM', '_',4,'nmod_adj','_','_'],
            [4, 'उक्ति',   'उक्ति',   'NN',  'NN',  '_',7,'k7','_','_'],
            [5, 'पर',    'पर',     'PSP', 'PSP', '_',4,'lwg_psp','_','_'],
            [6, 'विश्वास','विश्वास',   'NN',  'NN',  '_',7,'pof','_','_'],
            [7, 'करते',  'करते',    'VM',  'VM',  '_',1,'ccof','_','_'],
            [8, 'हैं',    'हैं',      'VAUX','VAUX','_',7,'lwg_vaux','_','_'],
            [9, 'तो',    'तो',     'CC',  'CC',  '_',0,'main','_','_'],
            [10,'कोस्टर',  'कोस्टर',  'NNPC','NNPC','_',11,'pof_cn','_','_'],
            [11,'डायमंड',  'डायमंड', 'NNP', 'NNP',  '_',13,'r6','_','_'],
            [12,'का',    'का',    'PSP', 'PSP',  '_',11,'lwg_psp','_','_'],
            [13,'चक्कर',  'चक्कर',  'NN',  'NN',  '_',15,'k1','_','_'],
            [14,'ज़रूर',   'ज़रूर',  'RB',   'RB',  '_',9,'ccof','_','_'],
            [15,'लगाइएगा','लगाइएगा','VM',   'VM',  '_',9,'ccof','_','_'],
            [16,'.','.','SYM','SYM','_',9,'rsym','_','_']]
"""
