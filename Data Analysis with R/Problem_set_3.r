# R script for Problem Set 3 in Data Analysis with R

library(ggplot2)
diamonds = diamonds

# types of variables
str(diamonds)

levels(diamonds$color)

# Create a histogram of the price of all the diamonds in the diamond data set.
qplot(x = price, data = diamonds, binwidth = 200,
      color = I('black'), fill = I('#F79420'))

summary(diamonds$price)

# Diamond Counts
sum(diamonds$price<500)
sum(diamonds$price<250)
sum(diamonds$price>=15000)

# Cheaper Diamonds
qplot(x = price, y = cut, data = diamonds, binwidth = 5, xlim=c(0,2000),
      color = I('black'), fill = I('#F79420')) 

# Price by Cut Histograms
qplot(x = price, data = diamonds, 
      color = I('black'), fill = I('#F79420')) +
    facet_wrap(~cut, ncol = 5)

# Price by Cut
by(diamonds$price, diamonds$cut, summary)
by(diamonds$price, diamonds$cut, max)

# Scales and Multiple Histograms
qplot(x = price, data = diamonds) + facet_wrap(~cut, scales = "free_y")

# Price per Carat by Cut
qplot(x = price/carat, data = diamonds, color = I('black'), fill = I('#F79420')) + 
    facet_wrap(~cut, scales="free_y") + scale_x_log10()

# Price Box Plots
qplot(x=cut, y=price, data=diamonds, geom = 'boxplot', ylim=c(0,8000))
qplot(x=clarity, y=price, data=diamonds, geom = 'boxplot', ylim=c(0,4500))
qplot(x=color,y=price, data=diamonds, geom = 'boxplot', ylim=c(0,3000))

# Interquartile Range - IQR
by(diamonds$price, diamonds$color, summary)
IQR(subset(diamonds, color == 'D')$price)
IQR(subset(diamonds, color == 'J')$price)

# Price per Carat Box Plots by Color
qplot(x=color,y=price/carat, data=diamonds, geom = 'boxplot')

# Carat Frequency Polygon
qplot(x = carat, data = diamonds, geom = 'freqpoly', binwidth=0.01) + 
    scale_x_continuous(breaks = seq(0,5, 0.1))