import pandas as pd


def del_nan(data):
    return data.dropna()


def _main():
    *data, = pd.read_csv("./data/train.csv"), pd.read_csv("./data/test.csv")
    pass


if __name__ == "__main__":
    main()
