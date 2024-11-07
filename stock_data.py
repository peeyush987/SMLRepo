import numpy as np
import math
import pandas as pd

def scale_range(x, input_range, target_range):
    """
    Rescale a numpy array from input to target range
    :param x: data to scale
    :param input_range: optional input range for data: default 0.0:1.0
    :param target_range: optional target range for data: default 0.0:1.0
    :return: rescaled array, incoming range [min,max]
    """
    range = [np.amin(x), np.amax(x)]
    x_std = (x - input_range[0]) / (1.0 * (input_range[1] - input_range[0]))
    x_scaled = x_std * (1.0 * (target_range[1] - target_range[0])) + target_range[0]
    return x_scaled, range

def train_test_split_linear_regression(stocks):
    """
    Split the data set into training and testing feature for Linear Regression Model
    :param stocks: whole data set containing ['Open','Close','Volume'] features
    :return: X_train, X_test, y_train, y_test, label_range
    """
    feature = []
    label = []

    # Convert dataframe columns to numpy arrays for scikit-learn
    for index, row in stocks.iterrows():
        feature.append([row['Item']])  # Ensure 'Item' exists in the DataFrame
        label.append([row['Close']])

    # Regularize the feature and target arrays and store min/max for rescaling later
    feature_bounds = [min(feature), max(feature)]
    feature_bounds = [feature_bounds[0][0], feature_bounds[1][0]]
    label_bounds = [min(label), max(label)]
    label_bounds = [label_bounds[0][0], label_bounds[1][0]]

    feature_scaled, feature_range = scale_range(np.array(feature), input_range=feature_bounds, target_range=[-1.0, 1.0])
    label_scaled, label_range = scale_range(np.array(label), input_range=label_bounds, target_range=[-1.0, 1.0])

    # Define Test/Train Split 80/20
    split = .315
    split = int(math.floor(len(stocks['Item']) * split))

    X_train = feature_scaled[:-split]
    X_test = feature_scaled[-split:]

    y_train = label_scaled[:-split]
    y_test = label_scaled[-split:]

    return X_train, X_test, y_train, y_test, label_range


def train_test_split_lstm(stocks, prediction_time=1, test_data_size=450, unroll_length=50):
    """
    Split the data set into training and testing feature for Long Short Term Memory Model
    :param stocks: DataFrame containing stock data
    :param prediction_time: number of days to predict
    :param test_data_size: size of test data to be used
    :param unroll_length: how long a window should be used for train test split
    :return: X_train, X_test, y_train, y_test
    """
    test_data_cut = test_data_size + unroll_length + 1

    # Ensure correct slicing
    x_train = stocks.iloc[:-prediction_time - test_data_cut].values
    y_train = stocks['Close'].iloc[prediction_time:-test_data_cut].values

    x_test = stocks.iloc[-test_data_cut:-prediction_time].values
    y_test = stocks['Close'].iloc[-test_data_cut + prediction_time:].values

    return x_train, x_test, y_train, y_test





def unroll(data, sequence_length=24):
    """
    Use different windows for testing and training to avoid information leakage in the data
    :param data: data set to be used for unrolling
    :param sequence_length: window length
    :return: data sets with different windows
    """
    result = []
    for index in range(len(data) - sequence_length):
        result.append(data[index: index + sequence_length])
    return np.asarray(result)
