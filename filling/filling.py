import pandas as pd

from . import fare


FILL_FUNC_LIST = [
    fare.fill,
]


def fill(df):
    _df = df.copy()
    for e in FILL_FUNC_LIST:
        _df = e(_df)

    return _df
