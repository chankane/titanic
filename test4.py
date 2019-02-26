import pandas as pd


df = pd.DataFrame([
    [4, 99,  2],
    [3,  None, 99],
    [None,  8,  7],
    [8,  None,  8]
], columns=["a", "b", "c"])

#print(type(df.loc[[True, True, False, False]]))
#print(type(df.loc[[False, True, False, False]]))
print(type(df["a"].isna()))
print(type(df[["a"]].isna().any()))
print(df[["a", "b"]].isna().any(axis=1))
