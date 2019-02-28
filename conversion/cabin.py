import pandas as pd


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


def _floor2num(floor):
    return ord(floor) - ord("A")


def _roomno2num(roomno):
    return int(row[0][1:])


def cabin2xyz(cabin):
    x, y, z = pd.np.nan, pd.np.nan, pd.np.nan

    if cabin is pd.np.nan or cabin == "":
        return x, y, z

    # y
    y = ord(e[0]) - ord("A")

    if len(e) < 2:
        return x, y, z

    # x, z
    roomno = int(cabin[1:])
    x = roomno % 2
    z = roomno

    return x, y, z


def _str2int(cabin):
    x, y, z = [], [], []

    for row in cabin:
        if row is pd.np.nan:
            continue
        ?
    return num_list


def conv_t(df):
    _df = df.copy()

    # Positions of seats (negative)
    x, y, z = [], [], []

    cabins = _df["Cabin"].str.split()
    print(_str2int(cabin))

    #for e in cabin.dropna():
    #    if len(e) >= 2:
    #        print(e)

    for row in cabin:
        if row is pd.np.nan:
            continue
        # x, y, z of each row
        x_row, y_row, z_row = [], [], []
        for e in row:
            y_row.append(ord(e[0]) - ord("A"))
            #n = conv_e(e[1:])
            #rz.append(n)
            #rx.append(int(n % 2 == 1))
        #x.append(rx[0])
        y.append(y_row[0])
        #z.append(rz[0])

    df2 = pd.DataFrame({
        #"Cabin_x": x,
        "Cabin_y": y,
        #"Cabin_z": z,
    })

    # del df["Cabin"]
    return pd.concat((df, df2), axis=1)


def conv(df):
    _df = df.copy()
    # Positions of seats
    x = pd.np.arange(len(_df))
    y = x * 2
    z = x ** 2

    _df["Cabin_x"] = x
    _df["Cabin_y"] = y
    _df["Cabin_z"] = z

    del _df["Cabin"]

    return _df


def main():
    #train = norm(train)
    df = pd.read_csv("./data/train.csv")

    conv_t(df)


if __name__ == "__main__":
    main()
