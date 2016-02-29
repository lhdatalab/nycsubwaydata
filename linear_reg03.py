import numpy as np
import pandas
import matplotlib.pyplot as plt
import sklearn.linear_model

# Normalize input features
def normalized_features(features):
    means = np.mean(features, axis=0)
    std_devs = np.std(features, axis=0)
    normalized_features = (features - means) / std_devs
    return means, std_devs, normalized_features

# Create linear regression model
def linear_regression(features, values):
    model = sklearn.linear_model.SGDRegressor(alpha=0.0001, average=False, epsilon=0.1, eta0=0.01,
             fit_intercept=True, l1_ratio=0.15, learning_rate='invscaling',
             loss='squared_loss', n_iter=3000, penalty='l2', power_t=0.25,
             random_state=None, shuffle=True, verbose=0, warm_start=False)

    results = model.fit(features, values)
    intercept = results.intercept_
    params = results.coef_
    return intercept, params

# Denormalize parameters
def recover_params(means, std_devs, norm_intercept, norm_params):
    intercept = norm_intercept - np.sum(means * norm_params / std_devs)
    params = norm_params / std_devs
    return intercept, params


# Create liner regression model
def predictions(dataframe):
    # Choose features and create dummy variables
    features = dataframe[['wspdi', 'tempi', 'rain']]
    num_features = len(features.columns)
    for column in ['UNIT', 'conds', 'hour', 'day_week']:
        dummy = pandas.get_dummies(dataframe[column], prefix=column)
        features = features.join(dummy)

    # Values (target values)
    values = dataframe['ENTRIESn_hourly']

    # Convert the two dataframes into numpy arrays so  that numpy functions can be used on them.
    features_array = features.values
    values_array = values.values

    # Normalize the features
    means, std_devs, normalized_features_array = normalized_features(features_array)

    # Perform gradient descent
    norm_intercept, norm_params = linear_regression(normalized_features_array, values_array)

    # Denormalize parameters
    intercept, params = recover_params(means, std_devs, norm_intercept, norm_params)

    # Print parameters of non-categorical features
    print intercept, params[0:num_features]
    # Use model to get predicted values
    predictions = intercept + np.dot(features_array, params)
    return predictions


# Read in input data
turnstile_data = pandas.read_csv("turnstile_weather_v2.csv")

# Get predictions
predictions_val = predictions(turnstile_data)
y_data = turnstile_data["ENTRIESn_hourly"]

# Calculate residuals
num = float(np.sum((y_data - predictions_val)**2))
dem = float(np.sum((y_data - np.mean(y_data))**2))
r_squared = 1 - (num/dem)
print r_squared

# Get reiduals summary statistics
print (y_data - predictions_val).describe()

# Plot residuals histogram
plt.figure()
plt.hist(x=(y_data - predictions_val), color='b', bins=30)
plt.title('Linear Regression Model Performance')
plt.xlabel('Residuals')
plt.ylabel('Frequency')
plt.show()





