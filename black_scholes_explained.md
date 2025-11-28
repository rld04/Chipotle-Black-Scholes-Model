# 🧮 Black-Scholes Model Explained

## What is the Black-Scholes Model?

The Black-Scholes model is a mathematical formula used to calculate the theoretical price of options. Developed by economists Fischer Black, Myron Scholes, and Robert Merton in 1973, it revolutionized options trading and earned Scholes and Merton the Nobel Prize in Economics in 1997.

## How Does It Work?

Black-Scholes calculates option prices by considering five key factors:

### 1. Current Stock Price (S)
The current market price of the underlying stock. For Chipotle (CMG), this is fetched in real-time from Yahoo Finance.

### 2. Strike Price (K)
The price at which you can buy (call) or sell (put) the stock when you exercise the option.

### 3. Time to Expiration (T)
The time remaining until the option expires, measured in years. For example, 30 days = 30/365 = 0.082 years.

### 4. Volatility (σ)
A measure of how much the stock price fluctuates. Higher volatility = higher option prices because there's more uncertainty (and opportunity).

### 5. Risk-Free Rate (r)
The return on a "safe" investment like US Treasury bonds. Currently around 4-5% annually.

## The Mathematics

### Call Option Formula

```
C = S₀N(d₁) - Ke^(-rT)N(d₂)
```

Where:
- C = Call option price
- S₀ = Current stock price
- K = Strike price
- r = Risk-free rate
- T = Time to expiration
- N() = Cumulative standard normal distribution
- e = Euler's number (≈2.71828)

### Put Option Formula

```
P = Ke^(-rT)N(-d₂) - S₀N(-d₁)
```

### Helper Variables

```
d₁ = [ln(S₀/K) + (r + σ²/2)T] / (σ√T)
d₂ = d₁ - σ√T
```

Where:
- ln() = Natural logarithm
- σ = Volatility (annualized)
- √T = Square root of time

## Understanding N(d₁) and N(d₂)

These represent probabilities from the normal distribution:

- **N(d₂)** ≈ Probability the option expires in-the-money
- **N(d₁)** ≈ Expected value factor (slightly higher than N(d₂))

## Why I Chose Black-Scholes

### Advantages

1. **Industry Standard** - Most widely used options pricing model in finance
2. **Fast Calculation** - Closed-form solution means instant results
3. **Educational Value** - Perfect for understanding option pricing fundamentals
4. **Proven Track Record** - Used by traders and market makers for 50+ years
5. **Mathematical Elegance** - Beautiful derivation from stochastic calculus

### Real-World Applications

- Options exchanges use it for pricing quotes
- Traders use it to identify mispriced options
- Risk managers use it for portfolio valuation
- Academics use it as a foundation for more complex models

## Limitations

The Black-Scholes model makes several assumptions that don't always hold in real markets:

### 1. Constant Volatility
**Assumption:** Volatility (σ) stays constant over time.

**Reality:** Volatility changes constantly. Markets can be calm one day and chaotic the next.

**Impact:** Can cause model to misprice options during volatile periods.

### 2. Log-Normal Distribution
**Assumption:** Stock prices fo