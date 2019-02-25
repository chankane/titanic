import pandas as pd
from sklearn.ensemble import RandomForestClassifier


def pred(train, test, x, y):
    train_x = train[x].values
    train_y = train[y].values
    test_x = test[x].values

    clf = RandomForestClassifier(
        random_state=0, n_estimators=100, verbose=True
    )
    clf = clf.fit(train_x, train_y)

    return clf.predict(test_x)


def _pred(train_x, train_y, test_x):
    clf = RandomForestClassifier(
        random_state=0, n_estimators=100, verbose=True
    )
    clf = clf.fit(train_x, train_y)
    return clf.predict(test_x)


def main():
    pass


if __name__ == "__main__":
    main()
