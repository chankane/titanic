import numpy as np
import pandas as pd

import pred
from conversion.conv import conv
from normalization.norm import norm
from labeling.labeling import label
from filling.filling import fill


def write(pred):
    pred.to_csv("result.csv")


def main():
    train = pd.read_csv("./data/train.csv", index_col="PassengerId")
    test = pd.read_csv("./data/test.csv", index_col="PassengerId")

    train_len = len(train)

    df = pd.concat((train, test), sort=False)

    df = label(df)

    df = conv(df)

    print(df.isna().sum())
    df = fill(df)
    print(df.isna().sum())

    print(df)

    #write(df.loc[train_len + 1:, ["Survived"]])


if __name__ == "__main__":
    main()
