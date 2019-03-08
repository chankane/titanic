kTrain <- "data/train.csv"
kTest <- "data/test.csv"
kData <- "data/data.csv"


# 結合して返すよ〜
ReadTrainAndTest <- function() {
  # "" を NA として読み込むためには na.strings の指定が必要
  train <- read.csv(kTrain, na.strings=(c("NA", "")))
  test <- read.csv(kTest, na.strings=(c("NA", "")))

  test$Survived <- NA # これしないと結合できない
  rbind(train, test)
}


ReadData <- function() {
  # "" を NA として読み込むためには na.strings の指定が必要
  read.csv(kData, na.strings=(c("NA", "")))
}


WriteData <- function(df) {
  write.csv(df, "data/data.csv", row.names=F)
}


CountNa <- function(df) {
  sapply(df, function(x) sum(is.na(x)))
}


# 1 つでも含まれてたらアウト
DropColumnsOfNa <- function(df) {
  df[CountNa(df) == 0]
}


ConvertFormulaToColumns = function(formula) {
  tmp <- all.vars(formula)
  tmp[!(tmp %in% "T")]
}