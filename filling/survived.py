# Fill "Survived"
import pandas as pd

import pred


#X = ["PassengerId", "Pclass", "Sex", "SibSp", "Parch"]
X = ["Pclass", "Sex", "SibSp", "Parch", "Fare", "Embarked", "Age"]
Y = ["Survived"]


def fill(df):
    _df = df.copy()

    nan_idx = _df[Y].isna().any(axis=1)

    # NaN is an float value and need to fill some integer value
    _df[Y] = _df.fillna(0)[Y].astype(int)

    train = _df[~nan_idx]
    test = _df[nan_idx]

    _df.loc[nan_idx, Y] = pred.pred(train, test, X, Y)

    return _df


def _main():
    pass


if __name__ == "__main__":
    main()
