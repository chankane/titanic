import pandas as pd


def del_nan(df):
    return df.dropna()


def fill_zero(df):
    return df.fillna(0)


def fill_mean(df):
    return df.dropna(df.mean())


def fill_median(df):
    return df.fillna(df.median())


def _main():
    pass


if __name__ == "__main__":
    main()
