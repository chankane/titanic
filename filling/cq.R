# 回帰分析で補間

library("robustbase")
source("util/util.R")


# 評価に使う列（とりま 4 次式）
kFormula <- list(
  # 行数を優先
  row.size.priority = Fare ~ (
    + poly(Pclass, 2, raw=T)
    + poly(SibSp,  4, raw=T)
    + poly(Parch,  4, raw=T)
    + Female
    + poly(Fare,  4, raw=T)
  ),
  # 列数を優先
  col.size.priority = Fare ~ (
    + poly(Pclass, 2, raw=T)
    + poly(Age,    4, raw=T)
    + poly(SibSp,  4, raw=T)
    + poly(Parch,  4, raw=T)
    + Female
    + C
    + Q
    + poly(Fare,  4, raw=T)
  )
)


f <- kFormula$row.size.priority
#f <- kFormula$col.size.priority

columns <- ConvertFormulaToColumns(f)

df <- ReadData()

train <- df[columns]
train <- train[complete.cases(train), ]

# maxit.scale=200 では収束しない
model <- lmrob(f, data=train, setting="KS2014", maxit.scale=500)

na.idx <- is.na(df$Fare)

df[na.idx, "Fare"] <- predict(model, df[na.idx, ])

df[na.idx, ]

WriteData(df)
