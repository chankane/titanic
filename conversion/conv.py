import pandas as pd

from . import xyz


CONV_FUNC_LIST = [
    xyz.conv,
]


def conv(df):
    _df = df.copy()
    for e in CONV_FUNC_LIST:
        _df = e(_df)

    return _df
