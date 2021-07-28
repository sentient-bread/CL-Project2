from functools import partial

def findkar(kar, const):
    """
    recursively looks for
    karaka kar in constituent const
    """
    if const[0].kar == kar:
        return const
    for child in const[1:]:
        f = findkar(kar, child)
        if f != None:
            return f
    return None

def findpsp(const):
    """
    looks for karak chihna
    in dependents of head
    only (non-recursive)
    """
    for child in const[1:]:
        if child[0].kar == 'lwg__psp':
            return child[0].spel
    return None
        
def mahakarak(replacement, const):
    const[0].spel = replacement
    for child in const[1:]:
        mahakarak('', child)

def k1(const):
    replacement_possibilities = ["कौन", "क्या", "किसने"]
    if findpsp(const) == 'ने':
        mahakarak(replacement_possibilities[2], const)
    else:
        mahakarak(replacement_possibilities[0], const)
    return True


def k1s(const):
    replacement_possibilities = ["कौन", "कैसा", "कैसे", "कैसी"]
    if const != [] and const[0].spel != "" and const[0].pos = 'JJ':
        repl = "कैस" + const[0].spel[-1]
        if repl in replacement_possibilities:
            mahakarak(repl, const)
        else:
            mahakarak("कैसा", const)
    else:
        mahakarak(replacement_possibilities[0], const)
    return True

def k2(const):
    replacement_possibilities = ["किसको", "क्या"]
    if findpsp(const) == 'को':
        mahakarak(replacement_possibilities[0], const)
    else:
        mahakarak(replacement_possibilities[1], const)
    return True


def k2p(const):
    replacement_possibilities = ["कहाँ", "किधर"]
    # note: "कहां" and "किधर" can be considered interchangable

    mahakarak(replacement_possibilities[0], const)
    return True

def k3(const):
    replacement_possibilities = ["किससे", "किसके द्वारा", "किससे होकर"]
    if findpsp(const) == 'के':
        mahakarak(replacement_possibilities[1], const)
    else:
        mahakarak(replacement_possibilities[0], const)
    return True


def rt(const):
    replacement_possibilities = ["किसके लिए", "क्यों"]

    mahakarak(replacement_possibilities[0], const)
    return True


def rh(const):
    replacement_possibilities = ["क्यों", ]

    mahakarak(replacement_possibilities[0], const)
    return True


def k5(const):
    replacement_possibilities = ["किससे", "कहाँ से", "किधर से"]
    mahakarak(replacement_possibilities[0], const)
    return True


def r6(const):
    replacement_possibilities = ["किसका", "किसके", "किसकी"]
    # here the ambiguity will be resolved by gender
    # and / or number and / or honorific
    suff = findpsp(const)
    if suff != None:
        mahakarak('किस'+suff, const)
    elif const != [] and const[0].spel != "":
        gen = const[0].spel[-1]
        mahakarak('किसक'+gen, const)
    return True


def k7p(const):
    replacement_possibilities = ["कहाँ", "किधर", "किसमें", "किसपर", "किसपे"]
    suff = findpsp(const)
    if suff != None:
        mahakarak('किस'+suff, const)
    else:
        mahakarak(replacement_possibilities[0],const)
    return True


def k7t(const):
    replacement_possibilities = ["कब", "किस दिन", "कौनसे दिन"]
    # the last two are interchangable
    # the first is a broader case of the other two

    mahakarak(replacement_possibilities[0], const)
    return True


def main(_):
    return None

# paper.extended()
def pof(const):
    replacement_possibilities = ["क्या"]
    mahakarak(replacement_possibilities[0], const)
    return True

def nmod__adj(const):
    replacement_possibilities = ["कैसा", "कैसे", "कैसी"]
    # if the gender can be determined from the adjective,
    # use it to find which possibility to use
    # else use masc कैसा by default
    if const != [] and const[0].spel != "":
        if const[0].pos == 'JJ':
            repl = "कैस" + const[0].spel[-1]
            if repl in replacement_possibilities:
                mahakarak(repl, const)
            else:
                mahakarak("कैसा", const)
        elif const[0].pos == 'QC' and const[0].spel != 'एक':
            mahakarak("कितने", const)
    return True
    
emp = partial(mahakarak, '')
