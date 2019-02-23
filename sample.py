import numpy as np
import pandas as pd
from sklearn import tree

import missing as ms


def norm(data):
    return MS_FUNC(replace(data))


def f(x):
    print(x)
    print(x.strip())
    return x.strip()


def main():
    df = pd.read_csv("./sample.csv", index_col="Id")
    df2 = pd.DataFrame([
        [1, 2, "3"],
        [4, 5, "6"],
        [7, 8, "9 8"],
    ], columns=("a", "b", "c"))

    df_len = len(df)

    #print(df)
    print(df2)

    #st = "hoge hoge hoge"
    # print(df2["c"].map(f))
    #print(st.split())
    #print(lambda x: [s.strip() for s in x.split(',')])


if __name__ == "__main__":
    main()
