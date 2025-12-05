# 🌯 Chipotle Black-Scholes Options Calculator
A simple Python tool that calculates the fair price of options using the Black-Scholes model with real-time data from Yahoo Finance.

![Python](https://img.shields.io/badge/python-3.7+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

## 🎯 Features

- Real-time stock data via Yahoo Finance API
- Black-Scholes option pricing model
- Probability of profit calculations
- Support for both CALL and PUT 

## How it works
The Black-Scholes model calculates option prices by combining:

- Stock Price: Current CMG price from Yahoo Finance
- Strike Price: The price you want
- Time: 30 days until expiration
- Volatility: Calculated using historical data of 1 year
- Risk-Free Rate: Current 10 year Treasury rate

## Customization
- strike_price | Change the targeted strike price
- days | Change the days until expiration

## Prerequisities
- Python 3.7 or newer
- pip package manager

# Required Dependencies
- Yfiannce
- Numpy
- Scipy

## Understanding the Output
- **Fair Option Price**: The theoretical price you should pay for the option
- **Probability of Profit**: Likelihood the option will be in the money at expiration
- **Breakeven Point**: The stock price level where you neither profit nor lose
