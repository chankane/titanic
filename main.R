options(width=180)

# import 的なやつ
library(rpart)
library(rpart.plot)


label = function(df) {
  # Sex
  # 順番間違えたら悲惨なことになるゾ
  df$Sex = gsub("female", 1, df$Sex)
  df$Sex = gsub("male", 0, df$Sex)

  # Embarked
  df$Embarked = gsub("C", 0, df$Embarked)
  df$Embarked = gsub("Q", 1, df$Embarked)
  df$Embarked = gsub("S", 2, df$Embarked)
  df
}

del_col = function(df) {
  df[, c("PassengerId", "Survived", "Pclass", "Sex", "SibSp", "Parch")]
}

train = read.csv("data/train.csv")
head(train)
train = label(train)
head(train)
train = del_col(train)
head(train)
model = rpart(Survived ~ ., data = train)

#model
#rpart.plot(model)

test = train[, c("PassengerId", "Pclass", "Sex", "SibSp", "Parch")]

pred = predict(model, test)
pred = round(pred)
ans = train[, "Survived"]
wrong = sum(xor(pred, ans))
wrong
wrong / length(train)
# 相関のグラフ
# pairs(iris, panel = panel.smooth)
