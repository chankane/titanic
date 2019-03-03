# ただのラベリング

source("util/util.R")

df <- ReadData()

# 順番を間違えると悲惨になる
df$Sex <- gsub("female", 1, df$Sex)
df$Sex <- gsub("male", 0, df$Sex)

# こうしないと文字データのまま
df$Sex <- as.numeric(df$Sex)

WriteData(df)
