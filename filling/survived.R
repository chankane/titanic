# ランダムフォレストで補間

library("randomForest")
source("util/util.R")


# 評価に使う列（とりま 4 次式）
kFormula <- list(
  # 行数を優先
  row.size.priority = Survived ~ (
    + Pclass
    + Age
    + SibSp
    + Parch
    + Fare
    + Female
    + C
    + Q
    + WasNa
  ),
  # 列数を優先
  col.size.priority = Survived ~ (
    + Pclass
    + Age
    + SibSp
    + Parch
    + Fare
    + Female
    + C
    + Q
    + WasNa
  ),
  # 関係なさそうな項を除外
  after.p.test = Survived ~ (
    + Pclass
    + Age
    + SibSp
    + Parch
    + Fare
    + Female
    + C
    + Q
    + WasNa
  )
)


#f <- kFormula$row.size.priority
f <- kFormula$col.size.priority
#f <- kFormula$after.p.test

columns <- ConvertFormulaToColumns(f)

df <- ReadData()
df$Survived <- as.factor(df$Survived)

train <- df[columns]
train <- train[complete.cases(train), ]

train$Survived <- as.factor(train$Survived)
#head(train, 20)

model <- randomForest(f, data=train)
#varImpPlot(model)

na.idx <- is.na(df$Survived)

df[na.idx, "Survived"] <- predict(model, df[na.idx, ])
df$Survived <- as.character(df$Survived)
df$Survived <- as.integer(df$Survived)
head(df[na.idx, ], 30)

#summary(model)

#WriteData(df)
