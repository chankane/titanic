import pandas as pd


df = pd.DataFrame([
    [1, 1,  1],
    [1,  None, 1],
    [None,  1,  1],
    [1,  None,  1]
], columns=["a", "b", "c"])

print(df*[3, 4, 5])
print(df)
