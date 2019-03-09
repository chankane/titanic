source("util/util.R")

df <- ReadData()
df.test <- read.csv("data/test.csv")

nrow(df)
nrow(df.test)
nrow(df[892:1309, ])

#df.test$Survived <- df[892:1309, "Survived"]

#head(df.test$PassengerId)
#head(df.test)

PassengerId <- df.test$PassengerId
Survived <- df[892:1309, "Survived"]

df.ans <- data.frame(PassengerId, Survived)

head(df.ans, 30)

write.csv(df.ans, "res.csv", row.names=F)