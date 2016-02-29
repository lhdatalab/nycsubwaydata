import pandas
import matplotlib.pyplot as plt

turnstile_data = pandas.read_csv("turnstile_weather_v2.csv")
turnstile_dow = turnstile_data.groupby(['day_week'], as_index=False)['ENTRIESn_hourly'].mean()
turnstile_hour = turnstile_data.groupby(['hour'], as_index=False)['ENTRIESn_hourly'].mean()

# Plot two bar charts for average entries by day of the week and hour
plt.figure(figsize = (8, 12))
plt.subplot(211)
plt.bar(turnstile_dow['day_week'], turnstile_dow['ENTRIESn_hourly'], width=0.5, align='center')
plt.legend()
plt.title('Trends in Daily NYC Subway Traffic')
plt.xlabel('Day of the Week')
plt.xticks(turnstile_dow.day_week, ("Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"))
plt.ylabel('Averagre Entries')

plt.subplot(212)
plt.bar(turnstile_hour['hour'], turnstile_hour['ENTRIESn_hourly'], width=2, align='center')
plt.legend()
plt.title('Trends in Hourly NYC Subway Traffic')
plt.xlabel('Hour')
plt.xticks(turnstile_hour.hour)
plt.ylabel('Averagre Entries')
plt.show()