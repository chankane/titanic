import pandas as pd


NAN_POS = pd.np.array([pd.np.nan, pd.np.nan, pd.np.nan])


def _cabin2pos(cabin):
    pos = NAN_POS.copy()

    if cabin is pd.np.nan:
        return pos

    # y
    pos[1] = ord(cabin[0]) - ord("A")

    if len(cabin) < 2:
        return pos

    # x, z
    roomno = int(cabin[1:])
    pos[0] = roomno % 2
    pos[2] = roomno

    return pos


# Mean
def _cabins2pos(cabins):
    if cabins is pd.np.nan:
        return NAN_POS.copy()
    pos_list = pd.np.array([_cabin2pos(e) for e in cabins])
    return pd.np.mean(pos_list, axis=0)


def conv(df):
    _df = df.copy()

    cabins_list = _df["Cabin"].str.split()

    # Positions of seats (negative)
    pos_list = pd.np.array([_cabins2pos(e) for e in cabins_list])

    df_pos_list = pd.DataFrame({
        "x": pos_list[:, 0],
        "y": pos_list[:, 1],
        "z": pos_list[:, 2],
    })

    del _df["Cabin"]
    return pd.concat((_df, df_pos_list), axis=1)


def main():
    df = pd.read_csv("./data/train.csv")
    print(conv(df))


if __name__ == "__main__":
    main()
