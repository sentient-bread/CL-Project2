# CL-Project2
Question generation from stories in Hindi

# Tree Structure
* The tree is represented in Python by a nested list.
* The first item in the list is the root of the tree.
* This is followed by the lists representing the subtrees of each of its children.

For example, the sentence `यदि आप इस उक्ति पर विश्वास करते हैं तो कोस्टर डयमंड का चक्कर ज़रूर लगाइएगा।` is parsed as follows:
```
[['1', 'यदि',   'यदि',    'CC',  'CC',  '_','9','vmod','_','_'],
['2', 'आप',   'आप',    'PRP', 'PRP', '_','7','k1','_','_'],
['3', 'इस',    'इस',    'DEM', 'DEM', '_','4','nmod_adj','_','_'],
['4', 'उक्ति',   'उक्ति',   'NN',  'NN',  '_','7','k7','_','_'],
['5', 'पर',    'पर',     'PSP', 'PSP', '_','4','lwg_psp','_','_'],
['6', 'विश्वास','विश्वास',   'NN',  'NN',  '_','7','pof','_','_'],
['7', 'करते',  'करते',    'VM',  'VM',  '_','1','ccof','_','_'],
['8', 'हैं',    'हैं',      'VAUX','VAUX','_','7','lwg_vaux','_','_'],
['9', 'तो',    'तो',     'CC',  'CC',  '_','0','main','_','_'],
['10','कोस्टर',  'कोस्टर',  'NNPC','NNPC','_','11','pof_cn','_','_'],
['11','डायमंड',  'डायमंड', 'NNP', 'NNP',  '_','13','r6','_','_'],
['12','का',    'का',    'PSP', 'PSP',  '_','11','lwg_psp','_','_'],
['13','चक्कर',  'चक्कर',  'NN',  'NN',  '_','15','k1','_','_'],
['14','ज़रूर',   'ज़रूर',  'RB',   'RB',  '_','9','ccof','_','_'],
['15','लगाइएगा','लगाइएगा','VM',   'VM',  '_','9','ccof','_','_'],
['16','.','.','SYM','SYM','_','9','rsym','_','_']]
```
and its tree representation is
```
[तो, [यदि, [करते, [आप], [उक्ति, [इस], [पर]], [विश्वास], [हैं]]], [ज़रूर], [लगाइएगा, [चक्कर, [डायमंड, [कोस्टर], [का]]]], [.]]
```
or
```
[wo                                                                                              ]
    [yaxi                                           ] [jZarUra] [lagAiegA                   ] [.]
        [karawe                                    ]                [cakkara               ]
            [Apa] [ukwi           ] [viSvAsa] [hEM]                     [dAyamaNda        ]
                      [isa] [para]                                          [kostara] [kA]
```
In Devanagari,
```
[तो                                                                             ]
   [यदि                                     ] [ज़रूर] [लगाइएगा                ] [.]
       [करते                               ]            [चक्कर             ]
           [आप] [उक्ति         ] [विश्वास] [हैं]                [डायमंड         ]
                    [इस] [पर]                                [कोस्टर] [का]
```

# Directory Structure
* `tree.py` converts parser output to tree rep and vice versa
* `rules.py` has the rules; imports from `tree.py`
* `trav.py` traverses the tree rep and returns a list of questions; imports `rules.py` and `tree.py`
* `config.py` stores constant global variables and settings; is imported by all files
* `main.py` is the heavy driver

# Todo
- [x] Function from tree rep to sentence
- [ ] Rules.py functions
- [x] Traversal (tree rep -> replace -> sentence)
- [ ] Main
