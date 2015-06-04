setwd('/Users/Cinkie/Documents/Nanodegree/Data Analysis with R')

statesInfo = read.csv('stateData.csv')

subset(statesInfo, state.region == 1)
statesInfo[statesInfo$state.region == 1,]

---------------------------------------------------------------------
reddit = read.csv('reddit.csv')

table(reddit$employment.status)
summary(reddit)
str(reddit)
levels(reddit$age.range)

library(ggplot2)
qplot(data=reddit, x=age.range)

# Setting levels of ordered factors
levels(reddit$age.range) = c("Under 18", "18-24", "25-34", "35-44", "45-54", "55-64", "65 or Above")
