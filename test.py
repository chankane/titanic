import pandas as pd

import missing as ms

CHERBOURG, QUEENSTOWN, SOUTHAMPTON = range(3)
MS_FUNC = ms.del_nan


def replace(data):
    conf = {
        "Sex": {"male": 0, "female": 1},
        "Embarked": {"C": CHERBOURG, "Q": QUEENSTOWN, "S": SOUTHAMPTON}
    }
    res = data.copy()
    for k, v in conf.items():
        print(k, v)
        res[k] = data[k].replace(v)
    return res


def norm(data):
    return replace(MS_FUNC(data))


def read():
    return pd.read_csv("./data/train.csv"), pd.read_csv("./data/test.csv")


def main():
    *data_list, = read()

    for i, e in enumerate(data_list):
        data_list[i] = norm(e)

    print(data_list[0].head())

if __name__ == "__main__":
    main()
