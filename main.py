import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

import pred
from conversion.conv import conv
from normalization.norm import norm
from labeling.labeling import label


"""
X = [
    "PassengerId", "Pclass", "Sex", "Age",
    "SibSp", "Parch", "Fare", "Embarked",
]
"""
X = [
    "PassengerId", "Pclass", "Sex",
    "SibSp", "Parch", "Fare",
]
Y = "Survived"


def write(pred, idx_offset=0):
    idx = np.arange(len(pred)) + idx_offset

    df = pd.DataFrame({
        X[0]: idx,
        Y[0]: pred,
    })
    df.to_csv("result.csv", index=None)


def fill(df):
    _df = df.copy()
    _df = fare.fill_norm(_df)
    return _df


def main():
    train = pd.read_csv("./data/train.csv", index_col="PassengerId")
    test = pd.read_csv("./data/test.csv", index_col="PassengerId")

    train_len = len(train)

    df = pd.concat((train, test), sort=False)

    df = label(df)

    df = conv(df)

    df = norm(df)
    print(df.head())
    # print(df.head())
    #print(df.isna().sum())

    #print(df.isna().sum())

    # df = fill(df)

    #print(df.isna().sum())

    #print(df.isna().sum())
    #train = cabin.conv_row(train)
    #test = cabin.conv_row(test)
    #train = df.iloc[:train_len]
    #test = df.iloc[train_len:]

    #write(pred.pred(train, test, X, Y), train_len + 1)


if __name__ == "__main__":
    main()
