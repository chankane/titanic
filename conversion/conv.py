import pandas as pd

from . import cabin


CONV_LIST = {
    "Cabin": cabin.conv,
}


def conv(df):
    _df = df.copy()
    for k, v in CONV_LIST.items():
        _df = _df.join(v(_df[k]))
        del _df[k]
    return _df
