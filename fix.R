source("util/util.R")

df.def <- ReadTrainAndTest()
df <- ReadData()

#tail(df.def)
tail(df)

df$Survived <- df.def$Survived
#df$X <- NULL

tail(df)

WriteData(df)
