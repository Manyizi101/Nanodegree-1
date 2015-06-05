# This file contains the R code for Data Analysis with R problem set 4
library(ggplot2)
data(diamonds)

# price vs. x
ggplot(aes(x=x, y = price), data = diamonds) + geom_point()

# Correlations
with(diamonds, cor.test(x,price))
with(diamonds, cor.test(y,price))
with(diamonds, cor.test(z,price))

# price vs. depth
ggplot(aes(x = depth, y = price), data=diamonds) + geom_point()

# Adjustments - price vs. depth
ggplot(aes(x = depth, y = price), data=diamonds) + 
    geom_point(alpha = 1/100) + 
    scale_x_discrete(breaks = seq(43,79,2))

# Correlation - price and depth
with(diamonds, cor.test(depth,price))

# price vs. carat
ggplot(aes(x=carat, y=price), data = diamonds) + 
    geom_point() + 
    xlim(0, quantile(diamonds$carat, 0.99))

# price vs. volume
diamonds$volume = diamonds$x * diamonds$y * diamonds$z
ggplot(aes(x=volume, y = price), data = diamonds) + geom_point()

# Correlations on Subsets
with(subset(diamonds, volume > 0 & volume < 800), cor.test(price, volume))

# Adjustments - price vs. volume
ggplot(aes(x=volume, y=price), data = subset(diamonds, volume > 0 & volume < 800)) + 
    geom_point(alpha = 0.05) + 
    geom_smooth(method = 'lm')

# Mean Price by Clarity
diamondsByClarity = diamonds %>%
    group_by(clarity) %>%
    summarise(mean_price = mean(price),
              median_price = median(as.numeric(price)),
              min_price = min(price),
              max_price = max(price),
              n = n()) %>%
    arrange(clarity)

# Bar Charts of Mean Price
library(gridExtra)
diamonds_by_color <- group_by(diamonds, color)
diamonds_mp_by_color <- summarise(diamonds_by_color, mean_price = mean(price))

diamonds_by_clarity <- group_by(diamonds, clarity)
diamonds_mp_by_clarity <- summarise(diamonds_by_clarity, mean_price = mean(price))

p1=ggplot(diamonds_mp_by_clarity, aes(clarity, mean_price)) + geom_bar(stat="identity")
p2=ggplot(diamonds_mp_by_color, aes(color, mean_price)) + geom_bar(stat="identity")

grid.arrange(p1,p2,ncol=2)