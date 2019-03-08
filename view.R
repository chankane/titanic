# 欠損値の個数を確認するためのスクリプト
source("util/util.R")


df <- ReadData()
#df <- ReadTrainAndTest()
CountNa(df)

#png("view.png")
#a <- rep(0, length(df$Fare))
#a[df$Embarked == "Q"] <- 1
#a[df$Embarked == "S"] <- 2
#hist(a)
#dev.off()
