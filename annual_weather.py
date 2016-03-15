import pandas
import matplotlib.pyplot as plt

# Get annual and monthly weather data for NYC in 2011
weather_data = pandas.read_csv("wunderground_2011_NYC.csv")
turnstile_data = pandas.read_csv("turnstile_weather_v2.csv")
weather_data[' Max Wind SpeedMPH'].describe()

wind_month = turnstile_data.groupby(['DATEn'], as_index=False)['wspdi'].mean()
temp_month = turnstile_data.groupby(['DATEn'], as_index=False)['tempi'].mean()


# Plot wind speed and temperature yearly and monthly distributions
plt.figure(figsize=(14,12))
plt.subplot(221)
weather_data[' Max Wind SpeedMPH'].plot(kind='hist', alpha=0.8, color='blue', label=None, bins=20, range=(0, 40))
plt.legend()
plt.title('Annual Wind Speed distribution')
plt.xlabel('Wind Speed')
plt.ylabel('Frequency')

plt.subplot(223)
wind_month['wspdi'].plot(kind='hist', alpha=0.8, color='green', label=None, bins=20, range=(0, 40))
plt.legend()
plt.title('Monthly Wind Speed distribution')
plt.xlabel('Wind Speed')
plt.ylabel('Frequency')
plt.ylim(0, 15)

plt.subplot(222)
weather_data['Mean TemperatureF'].plot(kind='hist', alpha=0.8, color='blue', label=None, bins=20, range=(0, 110))
plt.legend()
plt.title('Annual Temperature distribution')
plt.xlabel('Temperature')
plt.ylabel('Frequency')

plt.subplot(224)
temp_month['tempi'].plot(kind='hist', alpha=0.8, color='green', label=None, bins=20, range=(0, 110))
plt.legend()
plt.title('Monthly Temperature distribution')
plt.xlabel('Temperature')
plt.ylabel('Frequency')
plt.show()
