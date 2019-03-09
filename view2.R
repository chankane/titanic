source("util/util.R")


df <- ReadData()

length(df$Parch[df$Parch == 1])

png("age0.png")
hist(df$Age[df$Parch == 0])
dev.off()

png("age1.png")
hist(df$Age[df$Parch == 1])
dev.off()

png("age2.png")
hist(df$Age[df$Parch == 2])
dev.off()

png("age3.png")
hist(df$Age[df$Parch >= 3])
dev.off()