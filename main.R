Fig <- function(x, y, pred.x=NULL, pred.y=NULL, fname="Rplots.png") {
  png(fname)
  plot(x, y)
  if (is.null(pred.x) && is.null(pred.y)) {
    par(new=T)
    lines(pred.x, pred.y, col="red")
  }
  dev.off()
}


df <- read.csv("./data.csv")

colSums(is.na(df))

model1 <- lm(Fare ~ Pclass, data=df)
pred1 <- predict(model1)

pred1

# 欠けてないやつを使う
#Fig(df$PassengerId, df$Fare, fname="PassengerId.png")
Fig(df$Pclass, df$Fare, df$Pclass, pred1, fname="Pclass.png")
#Fig(df$Sex, df$Fare, fname="Sex.png")
#Fig(df$SibSp, df$Fare, fname="SibSp.png")
#Fig(df$Parch, df$Fare, fname="Parch.png")


# head(df)
