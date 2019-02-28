import pandas as pd

from . import fare
from . import embarked
from . import age
from . import survived


FILL_FUNC_LIST = [
    fare.fill,
    embarked.fill,
    age.fill,
    survived.fill,
]


def fill(df):
    _df = df.copy()
    for e in FILL_FUNC_LIST:
        _df = e(_df)

    return _df
