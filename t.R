cre_model = function(x, y) {
  # 1 次関数で近似
  f = y ~ a1*x^1 + a0*x^0
  nls(f, start=c(a1=0, a0=0))
}

train = read.csv("data/sample1.csv")
test = read.csv("data/sample2.csv")

# model = cre_model(train$X, train$Y)
x = train$X
y = train$Y
f = y ~ a1*x^1 + a0*x^0
model = nls(f, start=c(a1=0, a0=0), T)

pred = predict(model, test)
length(test$X)
length(pred)
