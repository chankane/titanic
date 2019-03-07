# 線形回帰分析で補間

source("util/util.R")


# 行数優先
ManyRow <- function(df) {
  df <- df[c("Fare", "Pclass", "SibSp", "Parch", "Female", "C")]
  df[is.na(df ]
}


df <- ReadData()

head(ManyRow(df))

#Fare <- df$Fare  # df$Fare を直接下に代入すると、df$Fare という名前の列ができる
#df.x = cbind(DropColumnsOfNa(df), Fare)

#model <- lm(df$Fare ~ ., data=ManyRow(df))

na.idx <- is.na(df$Fare)

#pred = predict(model, df[na.idx, ])

#df[na.idx, ] = pred

#WriteData(df)
