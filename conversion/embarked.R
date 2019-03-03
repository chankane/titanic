# ただのラベリング

source("util/util.R")

df <- ReadData()

df$Embarked <- gsub("C", 0, df$Embarked)
df$Embarked <- gsub("Q", 1, df$Embarked)
df$Embarked <- gsub("S", 2, df$Embarked)

# こうしないと文字データのまま
df$Embarked <- as.numeric(df$Embarked)
df$Embarked <- as.factor(df$Embarked)

WriteData(df)
#head(df$Embarked)
