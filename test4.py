import pandas as pd


df = pd.DataFrame({
    "Id": [1, 2, 3, 4, 5],
    "Name": ["A", "B", "C", "D", "E"],
    "Height": [180, 180, 180, 180, 180]
})

df = df.set_index("Id")

print(df)
print(df[["Name", "Height"]])
