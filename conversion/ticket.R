# 削除する

source("util/util.R")

df <- ReadData()

df$Ticket <- NULL

WriteData(df)
