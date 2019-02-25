import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import cabin

CHERBOURG, QUEENSTOWN, SOUTHAMPTON = range(3)


def replace(data):
    conf = {
        "Sex": {"male": 0, "female": 1},
        "Embarked": {"C": CHERBOURG, "Q": QUEENSTOWN, "S": SOUTHAMPTON}
    }
    res = data.copy()
    for k, v in conf.items():
        res[k] = data[k].replace(v)
    return res


train = pd.read_csv("./data/train.csv")
test = pd.read_csv("./data/test.csv")
df = pd.concat((train, test))
print(df.isna().sum())
#del df["Age"]
#df.dropna(inplace=True)
#df.reset_index(drop=True, inplace=True)
print(df)
df = replace(df)
df = cabin.conv_row(df)
print(df)
print(df.corr())
print(sns.heatmap(df.corr()))
plt.show()
