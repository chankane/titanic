bf <- read.csv("data/data.csv")

df <- read.csv("age.csv")
df2 <- read.csv("age2.csv")

df$x2 <- df2$x
df$y <- df$x - df$x2

head(df)

df <- df[df$y > -100, ]

df[df$y > 10, ]

hist(df$y)
