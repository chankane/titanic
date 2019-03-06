x <- 0:20
e <- rnorm(length(x))
y <- x + e

png("Rplots.png")

plot(x, y)

dev.off()
