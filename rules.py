from functools import partial


def mahakarak(replacement, const):
    const[0].spel = replacement
    for child in const[1:]:
        mahakarak('', child)


def main(_):
    return None


emp = partial(mahakarak, '')
