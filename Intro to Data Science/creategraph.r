setwd("/Users/Cinkie/Downloads")
library(ggplot2)
require(gridExtra)

df = read.csv("turnstile_weather_v2.csv")
df2 = read.csv("turnstile_data_master_with_weather.csv")

# plot of histograms, rain vs not rain
entry1 = ggplot(df[df$rain==0,], aes(x=ENTRIESn_hourly)) + geom_histogram(binwidth=100) + 
    ggtitle("Hourly Entries Histogram, non-rain") +xlim(0,15000) + ylim(0,2700)

entry2 = ggplot(df[df$rain==1,], aes(x=ENTRIESn_hourly)) + geom_histogram(binwidth=100) + 
    ggtitle("Hourly Entries Histogram, rain") +xlim(0,15000)+ ylim(0,2700)

grid.arrange(entry1, entry2, ncol=2)

# plot of histograms, rain vs not rain
entry221 = ggplot(df2[df2$rain==0,], aes(x=ENTRIESn_hourly)) + geom_histogram(binwidth=100) + 
    ggtitle("Hourly Entries Histogram, non-rain") +xlim(0,15000) + ylim(0,2700)

entry22 = ggplot(df2[df2$rain==1,], aes(x=ENTRIESn_hourly)) + geom_histogram(binwidth=100) + 
    ggtitle("Hourly Entries Histogram, rain") +xlim(0,15000)+ ylim(0,2700)

grid.arrange(entry221, entry22, ncol=2)

#scale_fill_discrete(name="rain",labels=c("non-rainy", "rainy"))

# plot of hours per day
avehr = as.data.frame(matrix(0,6,2))
avehr[,1] = c(0,4,8,12,16,20)
names(avehr) = c("hour", "Average_ENTRIESn_hourly")
for (i in 1:6){
    avehr[i,2] = mean(df$ENTRIESn_hourly[df$hour == avehr[i,1]])
}

p1=ggplot(avehr, aes(x=hour, y=Average_ENTRIESn_hourly)) + geom_line(size=1) + 
    ggtitle("Average Hourly Entries in Hour of Day")

# plot of day-of-week
avewk = as.data.frame(matrix(0,7,2))
avewk[,1] = 0:6
names(avewk) = c("Day", "Average_ENTRIESn_daily")
for (i in 1:7){
    avewk[i,2] = mean(df$ENTRIESn_hourly[df$day_week == avewk[i,1]])
}

p2=ggplot(avewk, aes(x=Day, y=Average_ENTRIESn_daily)) + geom_line(size=1) + 
    ggtitle("Average Hourly Entries in Day of Week")

grid.arrange(p1, p2, ncol=2)
