# ランダムフォレストで補間

library("randomForest")
source("util/util.R")


# 評価に使う列
kFormula <- list(
  # 行数を優先
  row.size.priority = Embarked ~ (
    + Pclass
    + SibSp
    + Parch
    + Fare
    + Female
  ),
  # 列数を優先
  col.size.priority = Embarked ~ (
    + Pclass
    + Age
    + SibSp
    + Parch
    + Fare
    + Female
  )
)


#f <- kFormula$row.size.priority
f <- kFormula$col.size.priority

columns <- ConvertFormulaToColumns(f)

df <- ReadData()

df$Embarked <- NA
df$Embarked[df$C == 1] <- "C"
df$Embarked[df$Q == 1] <- "Q"
df$Embarked[df$C + df$Q == 0] <- "S"
df$Embarked <- as.factor(df$Embarked)  # デフォルトだと character 型

train <- df[columns]
train <- train[complete.cases(train), ]

model <- randomForest(f, data=train)

na.idx <- is.na(df$Embarked)

df[na.idx, "Embarked"] <- predict(model, df[na.idx, ])

df$C <- as.integer(df$Embarked == "C")
df$Q <- as.integer(df$Embarked == "Q")

df$Embarked <- NULL

df[na.idx, ]

WriteData(df)
