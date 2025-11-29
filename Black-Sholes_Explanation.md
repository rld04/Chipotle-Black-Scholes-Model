# 🧮 Black-Scholes Model Explained

## What is the Black-Scholes Model?

The Black-Scholes model is a mathematical formula used to calculate the theoretical price of options assuming volatility is constant. Developed by economists Fischer Black, Myron Scholes, and Robert Merton in 1973.

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

2. Log-Normal Distribution
Assumption: Stock prices follow a log-normal distribution.
Reality: Real markets have "fat tails" - extreme events happen more often than the model predicts.
Impact: May underestimate risk of large price movements.
3. No Dividends
Assumption: The stock doesn't pay dividends.
Reality: Many stocks (including Chipotle occasionally) pay dividends.
Impact: Can be adjusted with dividend yield, but adds complexity.
4. European-Style Options
Assumption: Options can only be exercised at expiration.
Reality: American options can be exercised any time before expiration.
Impact: May underprice American options, especially for puts.
5. No Transaction Costs
Assumption: No fees, commissions, or taxes.
Reality: Every trade has costs that eat into profits.
Impact: Theoretical prices don't account for real trading costs.
6. Efficient Markets
Assumption: Markets are perfectly efficient and liquid.
Reality: There can be bid-ask spreads, liquidity issues, and market manipulation.
Impact: Prices in thin markets may deviate significantly.
Modern Improvements
Since 1973, many improvements have been developed:

Binomial/Trinomial Trees - Better for American options
Monte Carlo Simulation - Handles complex payoffs
Stochastic Volatility Models (Heston, SABR) - Accounts for changing volatility
Jump Diffusion Models - Accounts for sudden price jumps
Local Volatility Models - Volatility varies by strike and time

When to Trust Black-Scholes
Black-Scholes works best for:
-✅ Liquid, high-volume stocks (like CMG)

-✅ European-style options

-✅ Near-the-money options

-✅ Moderate time to expiration (30-90 days)

-✅ Normal market conditions
Black-Scholes is less reliable for:

-❌ Deep out-of-the-money options

-❌ Options with very short or very long expirations

-❌ During market crashes or extreme volatility

-❌ Illiquid stocks with wide bid-ask spreads
