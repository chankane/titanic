# x は 100 個
x = runif(100) * 100 - 50

# 係数たち
a3 = 0.01
a2 = 0.1
a1 = 1
a0 = 10

y = a3*x^3 + a2*x^2 + a1*x + a0

# ノイズを混ぜる
y = y + rnorm(100) * 100

plot(x, y)

# 非線形回帰分析
f = y ~ b3*x^3 + b2*x^2 + b1*x + b0
res = nls(f, start=c(b3=0, b2=0, b1=0, b0=0))
res

pred = predict(res, newdata=-50:50)
pred

par(new = T) # グラフを上書きって意味らしい
plot(x, pred, type = "l")
