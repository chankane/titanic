def norm(*args):
    if len(args) == 0:
        return None
    elif len(args) == 1:
        return NORM_FUNC(args[0])

    res = []
    for e in args:
        res.append(NORM_FUNC(e))
    return res


# Fill fare
# del col (not Embarked)
# ans = 7.5500
import pandas as pd
from sklearn.ensemble import RandomForestClassifier


CHERBOURG, QUEENSTOWN, SOUTHAMPTON = range(3)
X = ["PassengerId", "Pclass", "Sex", "SibSp", "Parch", "Embarked"]
Y = "Fare"


def replace(df):
    conf = {
        "Sex": {"male": 0, "female": 1},
        "Embarked": {"C": CHERBOURG, "Q": QUEENSTOWN, "S": SOUTHAMPTON}
    }
    res = df.copy()
    for k, v in conf.items():
        res[k] = df[k].replace(v)
    return res


def read():
    train = pd.read_csv("./data/train.csv")
    test = pd.read_csv("./data/test.csv")
    return pd.concat((train, test), sort=False)


def main():
    df = replace(read()).loc[:, X + [Y]]

    train = df.dropna()
    train_x = train[X].values
    train_y = (train[Y].values * 10000).astype(int)
    test = df[df[Y].isnull()]
    test_x = test[X].values
    #print(train)
    #print(test)
    print(train_x)
    print(train_y)
    print(test_x)

    clf = RandomForestClassifier(random_state=0, n_estimators=100, verbose=True)
    clf = clf.fit(train_x, train_y)

    pred = clf.predict(test_x)

    print(pred)


if __name__ == "__main__":
    for i in range(1):
        main()


# Fill fare
# del col (not Embarked + Age)
# ans = 7.8958
import pandas as pd
from sklearn.ensemble import RandomForestClassifier


CHERBOURG, QUEENSTOWN, SOUTHAMPTON = range(3)
X = ["PassengerId", "Pclass", "Sex", "SibSp", "Parch", "Embarked", "Age"]
Y = "Fare"


def replace(df):
    conf = {
        "Sex": {"male": 0, "female": 1},
        "Embarked": {"C": CHERBOURG, "Q": QUEENSTOWN, "S": SOUTHAMPTON}
    }
    res = df.copy()
    for k, v in conf.items():
        res[k] = df[k].replace(v)
    return res


def read():
    train = pd.read_csv("./data/train.csv")
    test = pd.read_csv("./data/test.csv")
    return pd.concat((train, test), sort=False)


def main():
    df = replace(read()).loc[:, X + [Y]]

    train = df.dropna()
    train_x = train[X].values
    train_y = (train[Y].values * 10000).astype(int)
    test = df[df[Y].isnull()]
    test_x = test[X].values
    #print(train)
    #print(test)
    print(train_x)
    print(train_y)
    print(test_x)

    clf = RandomForestClassifier(random_state=0, n_estimators=100, verbose=True)
    clf = clf.fit(train_x, train_y)

    pred = clf.predict(test_x)

    print(pred)


if __name__ == "__main__":
    for i in range(1):
        main()
