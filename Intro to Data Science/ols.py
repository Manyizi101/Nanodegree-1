import numpy as np
import pandas
import scipy
import statsmodels.api as sm
from patsy import dmatrices
import matplotlib.pyplot as plt
import pylab
import os

os.chdir('/Users/Cinkie/Downloads')
df = pandas.read_csv('turnstile_weather_v2.csv')

# adding UNIT as dummny variable
y, x = dmatrices('ENTRIESn_hourly ~ rain+meanprecipi+meantempi+\
            weekday+day_week+hour+UNIT', data=df,\
                     return_type='dataframe')

# fitting an OLS model
result = sm.OLS(y,x).fit()
predict = result.predict(x)
predict = pandas.DataFrame(predict)

# plot the correlation graph
fig = plt.figure(figsize=(8,5))
ax = fig.add_subplot(1,1,1)
ax.scatter(y, predict, color="red")
ax.set_title("Plot of 'ENTRIESn_hourly' vs fitted values")
ax.set_xlabel("'ENTRIESn_hourly'")
ax.set_ylabel("Fitted Values")
fig.savefig("scatter.png")

# plot the residual plot
fig = plt.figure()
#residual = y.values-predict.values
plt.plot(result.resid)
fig.suptitle('Residual Plot')
fig.savefig("residual.png")

# QQ plot
fig = plt.figure()
ax = fig.add_subplot(111)
stats.probplot(result.resid, plot=plt)
fig.savefig("qqplot.png")
