import pandas as pd


CHERBOURG, QUEENSTOWN, SOUTHAMPTON = range(3)


def conv_e(x):
    if x == "":
        return 0
    return int(x)


def conv_def(col):
    # Positions of seats(negative)
    x, y, z = [], [], []

    cabin = col.str.split()

    for c in cabin:
        if c is pd.np.nan:
            continue
        rx, ry, rz = [], [], []
        for e in c:
            ry.append(ord(e[0]) - ord("A"))
            n = conv_e(e[1:])
            rz.append(n)
            rx.append(int(n % 2 == 1))
        x.append(rx[0])
        y.append(ry[0])
        z.append(rz[0])

    df2 = pd.DataFrame({
        "Cabin_x": x,
        "Cabin_y": y,
        "Cabin_z": z,
    })

    # del df["Cabin"]
    return pd.concat((df, df2), axis=1)


def conv(col):
    # Positions of seats
    x = pd.np.arange(len(col))
    y = x * 2
    z = x ** 2

    return pd.DataFrame({
        "Cabin_x": x,
        "Cabin_y": y,
        "Cabin_z": z,
    }, index=col.index)


def main():
    #train = norm(train)
    df = pd.read_csv("./data/train.csv")

    print(df.head())
    df["Cabin"].fillna("A0", inplace=True)
    print(df.head())
    df = conv_row(df)
    print(df.head(10))
    print(df.dtypes)


if __name__ == "__main__":
    main()
