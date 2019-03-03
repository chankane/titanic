# 削除する

source("util/util.R")

df <- ReadData()

df$Name <- NULL

WriteData(df)
