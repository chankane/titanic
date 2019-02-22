def norm(*args):
    if len(args) == 0:
        return None
    elif len(args) == 1:
        return NORM_FUNC(args[0])

    res = []
    for e in args:
        res.append(NORM_FUNC(e))
    return res
