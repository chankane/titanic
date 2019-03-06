library("robustbase")


df <- read.csv("./data.csv")

# とりま2次式
f <- Fare ~ (
  + poly(PassengerId, degree=2, raw=T)
  + poly(Pclass, degree=2, raw=T)
  + poly(Sex, degree=2, raw=T)
  + poly(SibSp, degree=2, raw=T)
  + poly(Parch, degree=2, raw=T)
)

model <- lmrob(f, data=df)

df2 <- data.frame(
  Pclass = seq(1, 3, 0.01)
)

df2$Fare = predict(model, df2)

# 欠けてないやつを使う
#Fig(df$PassengerId, df$Fare, fname="PassengerId.png")
#Fig(df$Pclass, df$Fare, df2$Pclass, df2$Fare, df2$Pclass, df2$Fare2, fname="Pclass.png")
#Fig(df2$Pclass, df2$Fare, fname="Pclass2.png")
#Fig(df$Sex, df$Fare, fname="Sex.png")
#Fig(df$SibSp, df$Fare, fname="SibSp.png")
#Fig(df$Parch, df$Fare, fname="Parch.png")


# head(df)
