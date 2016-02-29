import pandas
import matplotlib.pyplot as plt

turnstile_data = pandas.read_csv("turnstile_weather_v2.csv")

# Setup subplot data
subs = [221, 222, 223, 224]
strvalue = ['precipi', 'pressurei', 'wspdi', 'tempi']
strgraph = ['Precipitation', 'Pressure', 'Wind Speed', 'Temperature']
histrange = [(-0.1, 0.5), (25, 32), (-0.1, 25), (45, 90)]
histbin = [50, 40, 20, 20]

# Plot subplots
plt.figure(figsize = (12, 12))
for i in range(0,4):
    plt.subplot(subs[i])
    plt.hist(x=turnstile_data[strvalue[i]], color='b', bins=histbin[i], range=(histrange[i]))
    plt.legend()
    plt.title(strgraph[i] + ' distribution')
    plt.xlabel(strgraph[i])
    if strvalue[i] == 'precipi':
        plt.ylim(0, 43000)
    plt.ylabel('Frequency')
plt.show()
