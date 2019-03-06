library("robustbase")
# library("psych")


# 行の数を優先で予測
ManyRow <- function(df) {
  # とりま2次式
  f <- Fare ~ (
    # row=T にしないとなんか勝手に正規化される
    + poly(Pclass, degree=2, raw=T)
    # + poly(Sex, degree=2, raw=T)
    + poly(SibSp, degree=2, raw=T)
    + poly(Parch, degree=2, raw=T)
  )

  model <- lmrob(f, data=df)

  predict(model, df[is.na(df$Fare), ])
}

df <- read.csv("./data.csv")
df$PassengerId <- NULL  # どの値との相関もゴミだった

df[is.na(df$Fare), ]
pred <- ManyRow(df)
pred
#pairs.panels(df)
