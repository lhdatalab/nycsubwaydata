import numpy as np
import pandas
import scipy.stats

turnstile_data = pandas.read_csv("turnstile_weather_v2.csv")

# Calculate MannWhitneyU statistics
rain_mean = np.mean(turnstile_data['ENTRIESn_hourly'][turnstile_data['rain'] == 1])
norain_mean = np.mean(turnstile_data['ENTRIESn_hourly'][turnstile_data['rain']== 0])
(U, p) = scipy.stats.mannwhitneyu(turnstile_data['ENTRIESn_hourly'][turnstile_data['rain'] == 1], turnstile_data['ENTRIESn_hourly'][turnstile_data['rain']== 0])

# Calculate MannWhitneyU manually as scipy.stats function returns nan
rain_data = turnstile_data.groupby('rain', as_index=False).size()
n1 = rain_data[1]
n2 = rain_data[0]

mu = (n1 * n2)/2
sigmau = np.sqrt((n1 * n2 * (n1 + n2 + 1))/12)
z =  (U - mu)/sigmau
p = 2*scipy.stats.norm.cdf(z)

print 'Rain mean = ', rain_mean
print 'No rain mean = ', norain_mean
print 'U statistic = ', U
print 'p-value = ', p



