# 線形回帰分析で補間
source("util/util.R")


df <- ReadData()

Fare <- df$Fare  # df$Fare を直接下に代入すると、df$Fare という名前の列ができる
df.x = cbind(DropColumnsOfNa(df), Fare)

model <- lm(df$Fare ~ ., data=df.x)

na.idx <- is.na(df$Fare)

pred = predict(model, df[na.idx, ])

df[na.idx, ] = pred

WriteData(df)
