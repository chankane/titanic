source("util/util.R")


df <- ReadData()
df.def <- ReadTrainAndTest()

idx <- is.na(df.def$Age) || is.na(df.def$Fare) || is.na(df.def$C)

sum(is.na(df.def$Female))
#df$WasNa <- as.integer(!complete.cases(df.def))
df$WasNa <- as.integer(idx)
#head(df.test$PassengerId)
head(df)
tail(df)

#WriteData(df)

#PassengerId <- df.test$PassengerId
#Survived <- df[892:1309, "Survived"]

#df.ans <- data.frame(PassengerId, Survived)

#head(df.ans, 30)

#write.csv(df.ans, "res.csv", row.names=F)