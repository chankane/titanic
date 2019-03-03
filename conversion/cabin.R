# 削除する

source("util/util.R")

df <- ReadData()

df$Cabin <- NULL

WriteData(df)
