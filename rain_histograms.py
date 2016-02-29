import pandas
import scipy.stats
import matplotlib.pyplot as plt

turnstile_data = pandas.read_csv("turnstile_weather_v2.csv")

# Sample size of rain and no rain data
rain_data = turnstile_data.groupby('rain', as_index=False).size()
print 'Sample size of rain and no rain data'
print 'No. of samples (no rain) = ', rain_data[0]
print 'No. of samples (rain) = ', rain_data[1]
print

# Test for a Normal distribution
(W, p) = scipy.stats.shapiro(turnstile_data['ENTRIESn_hourly'][turnstile_data['rain'] == 0])
print 'rain = 0'
print 'Shapiro-Wilcox statistic = ', W
print 'p-value = ', p
print
(W, p) = scipy.stats.shapiro(turnstile_data['ENTRIESn_hourly'][turnstile_data['rain'] == 1])
print 'rain = 1'
print 'Shapiro-Wilcox statistic = ', W
print 'p-value = ', p

# Plot historgram for hourly entries when it is raining
plt.figure()
turnstile_data['ENTRIESn_hourly'][turnstile_data['rain'] == 0].plot(kind='hist', alpha=0.8, color='blue', label='no_rain', bins=15, range=(0, 6000))
turnstile_data['ENTRIESn_hourly'][turnstile_data['rain'] == 1].plot(kind='hist', alpha=1, color='green', label='rain', bins=15, range=(0, 6000))
plt.legend()
plt.title('Subway traffic distribution')
plt.xlabel('No. of hourly entries')
plt.ylabel('Frequency')
plt.show()
