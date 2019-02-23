import pandas as pd


def del_nan(ser):
    return ser.dropna()


def fill_zero(ser):
    return ser.fillna(0)


def fill_mean(ser):
    return ser.fillna(ser.mean())


def fill_median(ser):
    return ser.fillna(ser.median())


def _main():
    pass


if __name__ == "__main__":
    main()
