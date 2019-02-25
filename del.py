import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

import missing as ms
import cabin


CHERBOURG, QUEENSTOWN, SOUTHAMPTON = range(3)
MS_FUNC = ms.del_nan


def replace(data):
    conf = {
        "Sex": {"male": 0, "female": 1},
        "Embarked": {"C": CHERBOURG, "Q": QUEENSTOWN, "S": SOUTHAMPTON}
    }
    res = data.copy()
    for k, v in conf.items():
        res[k] = data[k].replace(v)
    return res


def norm(df):
    t = MS_FUNC(replace(df))
    t.reset_index(drop=True, inplace=True)
    return t


def write(pred, idx_offset=0):
    idx = np.arange(len(pred)) + idx_offset

    data = np.array((idx, pred)).T

    res = pd.DataFrame(data, columns=("PassengerId", "Survived"))
    res.to_csv("result.csv", index=None)


def main():
    train = pd.read_csv("./data/train.csv")
    test = pd.read_csv("./data/test.csv")

    train_len = len(train)

    train = norm(train)
    test = norm(test)

    train = cabin.conv_row(train)
    test = cabin.conv_row(test)

    print(train.head())
    print(test.head())

    #exp = ["PassengerId", "Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked", "Cabin_g", "Cabin_f", "Cabin_l"]
    exp = ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked", "Cabin_y"]

    target = train["Survived"].values
    explain = train[exp].values

    clf = RandomForestClassifier(random_state=0, n_estimators=100, verbose=True)
    clf = clf.fit(explain, target)

    test_explain = test[exp].values
    pred = clf.predict(test_explain)

    write(pred, train_len + 1)


if __name__ == "__main__":
    main()
