x = runif(100)
y = 10 * x ^2 + 10 + rnorm(100)

plot(x, y, xlim = range(2*x), ylim = range(2*y))

f = y ~ a*x^2 + b*x + c
obj = nls(f, start = c(a = 0, b = 0, c = 0))
obj

df = data.frame(x = seq(0, 10, length = 1000))
yy = predict(obj, df)
length(df$x)
length(yy)

par(new = T)
plot(df$x, yy, type = "l", col = "darkred", lwd = 2,
     xlim = range(2*x), ylim = range(2*y), xlab = "", ylab = "")