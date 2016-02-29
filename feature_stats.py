import pandas

turnstile_data = pandas.read_csv("turnstile_weather_v2.csv")
turnstile_data.drop(turnstile_data[['UNIT', 'DATEn', 'TIMEn', 'ENTRIESn', 'EXITSn', 'EXITSn_hourly', 'datetime', 'weekday', 'station', \
                                    'latitude', 'longitude', 'conds', 'weather_lat', 'weather_lon']], axis=1, inplace=True)
station = turnstile_data.describe()
print station
