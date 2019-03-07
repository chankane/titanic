# 削除する

source("util/util.R")

df <- ReadData()

df$PassengerId <- NULL

WriteData(df)
