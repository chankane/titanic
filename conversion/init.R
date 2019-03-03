# train.csv と test.csv を結合したものを data.csv という名前で保存する

source("util/util.R")


df <- ReadTrainAndTest()
WriteData(df)
