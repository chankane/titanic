# 欠損値の個数を確認するためのスクリプト
source("util/util.R")
library("robustbase")

f4 = Age ~ poly(SibSp,  4, raw=T)
f3 = Age ~ poly(SibSp,  3, raw=T)
f2 = Age ~ poly(SibSp,  2, raw=T)
f1 = Age ~ poly(SibSp,  1, raw=T)

df <- ReadData()
#df <- ReadTrainAndTest()
CountNa(df)

# df[df$SibSp >= 6, ]

columns <- c("Age", "SibSp")

df <- ReadData()

train <- df[columns]
train <- train[complete.cases(train), ]

#model1 <- lmrob(f1, data=train, setting="KS2014", maxit.scale=500)
#model2 <- lmrob(f2, data=train, setting="KS2014", maxit.scale=500)
#model3 <- lmrob(f3, data=train, setting="KS2014", maxit.scale=500)
# maxit.scale=200 では収束しない
#model4 <- lmrob(f4, data=train, setting="KS2014", maxit.scale=500)

model1 <- lm(f1, data=train, setting="KS2014", maxit.scale=500)
model2 <- lm(f2, data=train, setting="KS2014", maxit.scale=500)
model3 <- lm(f3, data=train, setting="KS2014", maxit.scale=500)
# maxit.scale=200 では収束しない
model4 <- lm(f4, data=train, setting="KS2014", maxit.scale=500)

anova(model1, model2, model3, model4)
#anova(model4, model3, model2, model1)

test <- data.frame(SibSp = seq(0, 9, length=100))

head(test)

test$Age <- predict(model3, test)


png("view.png")
#a <- rep(0, length(df$Fare))
#a[df$Embarked == "Q"] <- 1
#a[df$Embarked == "S"] <- 2
#hist(a)
plot(df$SibSp, df$Age)
lines(test$SibSp, test$Age, col="red")
dev.off()
