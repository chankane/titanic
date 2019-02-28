import pandas as pd

from . import cabin


CONV_FUNC_LIST = [
    cabin.conv,
]


def conv(df):
    _df = df.copy()
    for e in CONV_FUNC_LIST:
        _df = e(_df)

    return _df
