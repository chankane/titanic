c <- 3
a1 <- 8
a2 <- 2
b1 <- 6
b2 <- 5

x <- -50:50
y <- c + a1*x + a2*x^2 + b1*x + b2*x^2

plot(x, y)
