# ランダムフォレストで補間
options(width=180)  # 改行されて長くなるのがヤなだけ

library(randomForest)

source("util/util.R")


df <- ReadData()
head(df)
na.idx <- is.na(df$Embarked)

Embarked <- df$Embarked  # df$Embarked を直接下に代入すると、df$Embarked という名前の列ができる
df.x = cbind(DropColumnsOfNa(df), Embarked)
df.x = df.x[!na.idx, ]

head(df.x)

model <- randomForest(df.x$Embarked ~ ., data=df.x)
model
pred = predict(model, df[na.idx, ])
pred
df[na.idx, ] = pred
#WriteData(df)
