import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

import missing as ms
import pred
import cabin
import fare


CHERBOURG, QUEENSTOWN, SOUTHAMPTON = range(3)
MS_FUNC = ms.fill_median
X = [
    "PassengerId", "Pclass", "Sex", "Age",
    "SibSp", "Parch", "Fare", "Embarked",
]
Y = ["Survived"]


def replace(df):
    conf = {
        "Sex": {"male": 0, "female": 1},
        "Embarked": {"C": CHERBOURG, "Q": QUEENSTOWN, "S": SOUTHAMPTON}
    }
    _df = df.copy()
    for k, v in conf.items():
        _df[k] = df[k].replace(v)
    return _df


def write(pred, idx_offset=0):
    idx = np.arange(len(pred)) + idx_offset

    df = pd.DataFrame({
        X[0]: idx,
        Y[0]: pred,
    })
    df.to_csv("result.csv", index=None)


def fill(df):
    _df = df.copy()
    #_df = fare.fill(_df)
    return MS_FUNC(_df)


def main():
    train = pd.read_csv("./data/train.csv")
    test = pd.read_csv("./data/test.csv")

    train_len = len(train)

    # Merge
    df = replace(pd.concat((train, test), sort=False))

    print(df.head())

    #print(df.isna().sum())

    df = fill(df)

    print(df.isna().sum())
    #train = cabin.conv_row(train)
    #test = cabin.conv_row(test)
    train = df.iloc[:train_len]
    test = df.iloc[train_len:]

    write(pred.pred(train, test, X, Y), train_len + 1)


if __name__ == "__main__":
    main()
