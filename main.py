import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

import pred
from conversion.conv import conv

LABEL_COL = ["Sex", "Embarked"]
#LABEL_COL = ["Sex"]
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


def label(df):
    _df = df.copy()
    le = LabelEncoder()
    for col in LABEL_COL:
        # Not NaN index
        idx = ~_df[col].isna()
        _df.loc[idx, col] \
            = le.fit(_df.loc[idx, col]).transform(_df.loc[idx, col])
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
    _df = fare.fill_norm(_df)
    return _df


def main():
    train = pd.read_csv("./data/train.csv", index_col="PassengerId")
    test = pd.read_csv("./data/test.csv", index_col="PassengerId")

    train_len = len(train)

    df = pd.concat((train, test), sort=False)

    df = label(df)

    df = conv(df)
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
