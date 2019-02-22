import numpy as np
import pandas as pd
from sklearn import tree

import missing as ms

CHERBOURG, QUEENSTOWN, SOUTHAMPTON = range(3)
# MS_FUNC = ms.del_nan
MS_FUNC = ms.fill_zero


def replace(data):
    conf = {
        "Sex": {"male": 0, "female": 1},
        "Embarked": {"C": CHERBOURG, "Q": QUEENSTOWN, "S": SOUTHAMPTON}
    }
    res = data.copy()
    for k, v in conf.items():
        res[k] = data[k].replace(v)
    return res


def norm(data):
    return replace(MS_FUNC(data))


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

    target = train["Survived"].values
    # explain = train[["Pclass", "Sex", "Age", "Fare"]].values
    explain = train[["PassengerId"]].values
    d_tree = tree.DecisionTreeClassifier()
    d_tree = d_tree.fit(explain, target)

    # test_explain = test[["Pclass", "Sex", "Age", "Fare"]].values
    test_explain = test[["PassengerId"]].values
    pred = d_tree.predict(test_explain)

    write(pred, train_len + 1)


if __name__ == "__main__":
    main()
