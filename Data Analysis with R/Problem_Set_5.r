# This file contains R code for Data analysis with R Problem Set 5
library(ggplot2)
library(dplyr)
library(reshape2)
data(diamonds)

# Price Histograms with Facet and Color
ggplot(diamonds, aes(x = price, fill = cut)) + 
    geom_histogram(binwidth=200) + 
    scale_fill_brewer(type = 'qual') + 
    facet_wrap(~color) 

# Price vs. Table Colored by Cut
ggplot(diamonds, aes(x = table, y = price)) + 
    geom_point(aes(color = cut), size = 4) + 
    scale_color_brewer(type = 'qual') 

# Typical Table Value
by(diamonds$table, diamonds$cut, summary)

# Price vs. Volume and Diamond Clarity
diamonds = transform(diamonds, volume = x*y*z)
ggplot(diamonds, aes(x=volume, y=price)) + 
    geom_point(aes(color = clarity)) + 
    scale_y_log10() + 
    xlim(0,quantile(diamonds$volume, 0.99)) +
    scale_color_brewer(type = 'div')

# Proportion of Friendships Initiated
setwd('/Users/Cinkie/Documents/Nanodegree/Data Analysis with R')
pf = read.csv('pseudo_facebook.tsv', sep = '\t')
pf = transform(pf, prop_initiated=ifelse(friend_count==0,NA,friendships_initiated/friend_count))

# prop_initiated vs. tenure
ggplot(subset(pf, !is.na(prop_initiated) & !is.na(tenure)), 
       aes(x=tenure, y=prop_initiated)) + 
    geom_line(aes(color=year_joined.bucket), 
              stat='summary', fun.y = median)

# Smoothing prop_initiated vs. tenure
ggplot(subset(pf, !is.na(prop_initiated) & !is.na(tenure)), 
       aes(x=tenure, y=prop_initiated)) + 
    geom_line(aes(color=year_joined.bucket), 
              stat='summary', fun.y = median) +
    geom_smooth()

# Largest Group Mean prop_initiated
mean(subset(pf, year_joined.bucket == "(2012,2014]")$prop_initiated, na.rm=TRUE)

# Price/Carat Binned, Faceted, & Colored
ggplot(diamonds, aes(x=cut, y=price/carat)) +
    geom_point(aes(color=color)) +
    facet_wrap(~clarity) +
    scale_color_brewer(type = 'div')

