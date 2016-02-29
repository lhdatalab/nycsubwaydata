import pandas
import matplotlib.pyplot as plt

turnstile_data = pandas.read_csv("turnstile_weather_v2.csv")

# Get hourly traffic at each station
station = turnstile_data.groupby(['longitude', 'latitude'], as_index=False)['ENTRIESn_hourly'].mean().sort_values(['ENTRIESn_hourly'], ascending=False)

# Plot scatterplot of hourly subway traffic. Size of dots is the average hourly entries.
plt.figure()
plt.scatter(x=station['latitude'], y=station['longitude'], s=(station['ENTRIESn_hourly'])/20, alpha=0.6, color='blue', label=None)
plt.legend()
plt.title('Average hourly subway traffic by location')
plt.xlabel('Latitude')
plt.xlim(40.55, 40.9)
plt.ylabel('Longitude')
plt.show()

