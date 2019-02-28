import pandas as pd

from pred import pred


df = pd.DataFrame({
    "Id": [1, 2, 3, 4, 5],
    "Weight": [0.6, 0.7, 0.8, 0.9, 1.0],
    "Height": [160, 170, 180, None, 200]
})

df = df.set_index("Id")

print(df)

train = df.loc[[1, 2, 3, 5]]
test = df.loc[[4]]
x = ["Weight"]
y = ["Height"]
p = pred(train, test, x, y)
print(p)
print(None * 3)
