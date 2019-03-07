# 線形回帰分析で補間
library("robustbase")
source("util/util.R")


# 評価に使う列
kCol <- list(
  row = c("Fare", "Pclass", "SibSp", "Parch", "Female"),  # 行数を優先
  col = c("Fare", "Pclass", "Age", "SibSp", "Parch", "Female", "C", "Q")  # 列数を優先
)

df <- ReadData()

train <- df[kCol$row]
train <- train[complete.cases(train), ]

#model <- lmrob(Fare ~ Pclass + SibSp + Parch + Female, data=train)  # 1
#model <- lmrob(Fare ~ poly(Pclass, 2) + poly(SibSp, 2) + poly(Parch, 2) + Female, data=train)  # 2
#model <- lmrob(Fare ~ poly(Pclass, 2) + poly(SibSp, 3) + poly(Parch, 3) + Female, data=train)  # 3
model <- lmrob(Fare ~ poly(Pclass, 2) + poly(SibSp, 4) + poly(Parch, 4) + Female, data=train)  # 4

model

na.idx <- is.na(df$Fare)

df[na.idx, "Fare"] <- predict(model, df[na.idx, ])

df[na.idx, ]

#WriteData(df)
