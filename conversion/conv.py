import pandas as pd

from . import cabin


CONF = {
    "Cabin": cabin.conv,
}


def conv(df):
    _df = df.copy()
    for k, v in CONF.items():
        _df = _df.join(v(_df[k]))
        del _df[k]
    return _df
