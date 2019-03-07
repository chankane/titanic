# 質的データを量的データに変換

source("util/util.R")

df <- ReadData()

# 女性は 1
df$Female <- as.integer(df$Sex == "female")

df$Sex <- NULL

WriteData(df)
