import yfinance as yf
import numpy as np
from scipy.stats import norm

# Get Chipotle stock data
cmg = yf.Ticker("CMG")
stock_price = cmg.history(period="5d")['Close'].iloc[-1]

# Get volatility (standard deviation of returns)
hist = cmg.history(period="1y")
returns = np.log(hist['Close'] / hist['Close'].shift(1))
volatility = returns.std() * np.sqrt(252)

# Get risk-free rate (10-year Treasury)
treasury = yf.Ticker("^TNX")
risk_free_rate = treasury.history(period="5d")['Close'].iloc[-1] / 100

# Your parameters
strike_price = 35  # Strike price you want
days = 30  # 30 days until expiration
time_to_expiry = days / 365

# Ask if betting FOR or AGAINST the stock
print("=" * 50)
print("CHIPOTLE OPTIONS CALCULATOR")
print("=" * 50)
print(f"Current CMG Stock Price: ${stock_price:.2f}")
print(f"Strike Price: ${strike_price:.2f}")
print(f"Days Until Expiration: {days}")
print(f"Volatility: {volatility*100:.2f}%")
print(f"Risk-Free Rate: {risk_free_rate*100:.2f}%")
print()

bet_direction = input("Are you betting FOR or AGAINST the stock? (for/against): ").lower()

# Black-Scholes Formula
d1 = (np.log(stock_price / strike_price) + (risk_free_rate + 0.5 * volatility**2) * time_to_expiry) / (volatility * np.sqrt(time_to_expiry))
d2 = d1 - volatility * np.sqrt(time_to_expiry)

if bet_direction == "for":
    # CALL option (betting stock goes UP)
    option_price = stock_price * norm.cdf(d1) - strike_price * np.exp(-risk_free_rate * time_to_expiry) * norm.cdf(d2)
    probability = norm.cdf(d2) * 100
    print("\n📈 CALL OPTION (Betting stock goes UP)")
    print(f"Fair Option Price: ${option_price:.2f}")
    print(f"Probability of Profit: {probability:.2f}%")
    print(f"You make money if CMG > ${strike_price:.2f} at expiration")
    
elif bet_direction == "against":
    # PUT option (betting stock goes DOWN)
    option_price = strike_price * np.exp(-risk_free_rate * time_to_expiry) * norm.cdf(-d2) - stock_price * norm.cdf(-d1)
    probability = norm.cdf(-d2) * 100
    print("\n📉 PUT OPTION (Betting stock goes DOWN)")
    print(f"Fair Option Price: ${option_price:.2f}")
    print(f"Probability of Profit: {probability:.2f}%")
    print(f"You make money if CMG < ${strike_price:.2f} at expiration")

else:
    print("Invalid input. Please enter 'for' or 'against'")

print("\n" + "=" * 50)