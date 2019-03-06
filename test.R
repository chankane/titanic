# library("robustbase")

x <- 0:50
y <- 2*x + x^2# + rnorm(length(x)) * 50

model <- lm(y ~ poly(x, degree=2, raw=T) - 1)
#model22 <- lmrob(y ~ poly(x, degree=2))

model
yy <- predict(model)
#yy22 <- predict(model22)

plot(y)
lines(yy, col="red")
#lines(yy22, col="blue")
