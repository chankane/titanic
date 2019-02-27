# Fill fare
# ans = 78958
import pandas as pd

import pred
import main as m


X = ["PassengerId", "Pclass", "Sex", "SibSp", "Parch"]
Y = ["Fare"]


# NaN is an float value and need to fill some integer value
def _norm(df):
    _df = df.copy()
    _df[Y] = (_df.fillna(0)[Y] * 10000).astype(int)
    return _df


def fill_norm(df):
    nan_idx = df[Y].isna().any(axis=1)
    _df = _norm(df.copy())

    _df.loc[nan_idx, Y] = _main(_df, nan_idx)

    return _df


def _main(df, nan_idx):
    _df = df.copy()

    train = _df[~nan_idx]
    test = _df[nan_idx]

    return pred.pred(train, test, X, Y)


if __name__ == "__main__":
    df = m.replace(read()).loc[:, X + [Y]]
    print(main(df))
