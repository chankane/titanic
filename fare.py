# Fill fare
# del col
# ans = 7.8958
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

import pred
import main as m


X = ["PassengerId", "Pclass", "Sex", "SibSp", "Parch"]
Y = "Fare"


def fill(df):
    _df = df.copy()

    row = _df[_df[Y].isnull()].index.values
    col = Y

    _df.loc[row, col] = main(_df)

    return _df


def main(df):
    #normed_df = df.copy()
    #normed_df
    train = df.dropna(subset=[Y])
    train_x = train[X].values
    train_y = (train[Y].values * 10000).astype(int)

    test = normed_df[normed_df[Y].isnull()]
    test_x = test[X].values

    #return pred.pred(train_x, train_y, test_x) / 10000
    return pred.pred(train, test, X, Y)


if __name__ == "__main__":
    df = m.replace(read()).loc[:, X + [Y]]
    print(main(df))
