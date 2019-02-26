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
    df = pd.DataFrame({
        "Age": [10, 20, 30, 40, 50],
        "Blood": [1, 4, 2, 1, 3],
        "Height": [110, 120, 130, None, 150],
        "Height2": [120, 220, 230, None, 250],
    })

    train = df.iloc[[0]]
    test = df.iloc[3]
    x = ["Age", "Blood"]
    y = ["Height", "Height2"]

    print(_test(train, test, x, y))


if __name__ == "__main__":
    main()
