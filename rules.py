

def k1s(const):
    replacement_possibilities = ["कौन", "कैसा"]
    mahakarak(replacement_possibilities[0], const)


def k2p(const):
    replacement_possibilities = ["कहां", "किधर"]
    # note: "कहां" and "किधर" can be considered interchangable

    mahakarak(replacement_possibilities[0], const)


def rt(const):
    replacement_possibilities = ["किसके लिए", "क्यों"]

    mahakarak(replacement_possibilities[0], const)


def rh(const):
    replacement_possibilities = ["क्यों",]

    mahakarak(replacement_possibilities[0], const)


def r6(const):
    replacement_possibilities = ["किसका", "किसके", "किसकी"]
    # here the ambiguity will be resolved by gender and / or number and / or honorific

    mahakarak(replacement_possibilities[0], const)


def k7t(const):
    replacement_possibilities = ["कब", "किस दिन", "कौनसे दिन"]
    # the last two are interchangable
    # the first is a broader case of the other two

    mahakarak(replacement_possibilities[0], const)


