import pandas as pd

c = pd.read_csv("./data/train.csv")["Cabin"].unique()
cc = pd.read_csv("./data/test.csv")["Cabin"].unique()
print(c[:, None])
print(cc[:, None])
