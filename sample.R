f <- y ~ x1 + x2 + poly(x3, 3, raw=T) + poly(x4, 5, raw=T)

a <- all.vars(f)
a[-which(a %in% c("y", "T"))]
#terms(f)