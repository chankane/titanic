# 質的データを量的データに変換

source("util/util.R")

df <- ReadData()

df$C <- as.integer(df$Embarked == "C")
df$Q <- as.integer(df$Embarked == "Q")

df$Embarked <- NULL

head(df)

WriteData(df)
