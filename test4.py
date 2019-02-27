import pandas as pd


df = pd.DataFrame([
    [4, 99,  2],
    [3,  None, 99],
    [None,  8,  7],
    [8,  None,  8]
], columns=["a", "b", "c"])


def hi():
    A = 0
    return A

#print(type(df.loc[[True, True, False, False]]))
#print(type(df.loc[[False, True, False, False]]))
for i, e in enumerate(df):
    print(i, e)
    print(type(e))

print(hi())
