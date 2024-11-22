# Stock Price Prediction using Machine Learning

This project presents a comprehensive analysis and implementation of stock price prediction using machine learning techniques. The primary goal is to develop predictive models that can forecast stock prices based on historical data. We apply different machine learning algorithms, including Long Short-Term Memory (LSTM) networks and Linear Regression, to predict stock prices for Edwards Lifesciences Corporation (EW).

## Table of Contents
- [Introduction](#introduction)
- [Data Description](#data-description)
- [Methodology](#methodology)
  - [Data Preprocessing](#data-preprocessing)
  - [Model Development](#model-development)
- [Results](#results)
  - [Evaluation Metrics](#evaluation-metrics)
  - [Graphical Representations](#graphical-representations)
- [Discussion](#discussion)
- [Conclusion](#conclusion)
- [How to Run](#how-to-run)
- [Requirements](#requirements)

## Introduction
Stock price prediction is an important field of financial analytics, aimed at helping investors make informed decisions. In this project, we use historical stock data for Edwards Lifesciences Corporation (EW) to predict future stock prices. The project utilizes machine learning algorithms to develop predictive models, including **LSTM (Long Short-Term Memory)** networks and **Linear Regression**.

## Data Description
The dataset used in this project is sourced from **Kaggle** and contains daily stock prices for **Edwards Lifesciences Corporation (EW)**. The dataset includes the following columns:

- **Date**: The trading date.
- **Open**: The opening price of the stock.
- **Close**: The closing price of the stock.
- **High**: The highest price of the stock during the trading day.
- **Low**: The lowest price of the stock during the trading day.
- **Volume**: The total trading volume.

## Methodology

### Data Preprocessing
1. **Cleaning**: Handling missing values and removing unnecessary columns.
2. **Normalization**: Scaling the data using Min-Max scaling to ensure that all features contribute equally to the model.
3. **Feature Engineering**: Creating new features that may help improve prediction accuracy.

### Model Development
1. **Linear Regression Model**: A basic regression model to establish a baseline performance.
2. **LSTM Model**: A deep learning approach to capture temporal dependencies in the data.

### Train-Test Split
- The dataset is split into training and testing sets using an 80-20 split.
- The LSTM model requires unrolling of the data for time series forecasting.

## Results

### Evaluation Metrics
- **Mean Squared Error (MSE)**: Used to evaluate the performance of the models.

### Graphical Representations
1. **Plot of Closing Prices and Trading Days**: Visualization of the stock's closing prices over time.
2. **Plot of Trading Days and Closing Prices After Normalization**: Normalized data to ensure model stability.
3. **Plots of Actual vs Predicted Values**:
   - Using **Linear Regression** model.
   - Using **LSTM** model.

## Discussion
The **LSTM model** outperformed the **Linear Regression model**, demonstrating the effectiveness of deep learning techniques in capturing the temporal dependencies of stock prices. While the models achieved reasonable accuracy, it is important to consider that stock prices are influenced by a variety of external factors (e.g., market trends, political events, etc.), and these models are not sufficient for practical trading decisions alone.

## Conclusion
This project demonstrates the application of machine learning for stock price prediction. While the models show promise, future work could involve enhancing the models by incorporating additional features such as technical indicators (e.g., moving averages, RSI) and external data sources like sentiment analysis from news articles or social media.


