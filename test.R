Fig = function(raw, pred.x, pred.y) {
  # Plot Figure
  png("Rplots.png")
  plot(raw)
  par(new=T)
  lines(pred.x, pred.y, col="red")
  dev.off()  # Close deveice
}


f1 <- dist ~ speed
f2 <- dist ~ poly(speed, digree=2)
f3 <- dist ~ poly(speed, digree=3)
f4 <- dist ~ poly(speed, digree=4)
f5 <- dist ~ poly(speed, digree=5)
f6 <- dist ~ poly(speed, digree=6)

x <- seq(-50, 50, 0.5)
y <- 10 + x + 0.1*x^2 + 0.01*x^3 + rnorm(length(x))*200

mars = data.frame(
  speed = x,
  dist = y
)

model1 = lm(f1, data=mars)
model2 = lm(f2, data=mars)
model3 = lm(f3, data=mars)
model4 = lm(f4, data=mars)
model5 = lm(f5, data=mars)
model6 = lm(f6, data=mars)

pred1 = predict(model1)
pred2 = predict(model2)
pred3 = predict(model3)
pred4 = predict(model4)
pred5 = predict(model5)
pred6 = predict(model6)

anova(model1, model2, model3, model4, model5, model6)

Fig(mars, mars$speed, pred3)
