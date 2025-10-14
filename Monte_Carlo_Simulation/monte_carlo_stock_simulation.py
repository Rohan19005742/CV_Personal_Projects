'''
I will be simulating stock prices using the Monte Carlo method.
'''

import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

def monte_carlo_stock_simulation(ticker, num_simulation, num_days):
    data = yf.download(ticker, start="2020-01-01", end="2025-01-01")
    avg_daily_return = data["Close"].pct_change().mean()
    daily_volatility = data["Close"].pct_change().std()

    average_predected_price_per_simulation = []

    for sim in range(num_simulation):
        price_series = [data["Close"].iloc[-1]]
        for day in range(num_days):
            shock = np.random.normal(loc=avg_daily_return, scale=daily_volatility)
            price = price_series[-1] * (1 + shock)
            price_series.append(price)
        plt.plot(price_series)

        average_predected_price_per_simulation.append(np.mean(price_series))
    
    print(f"Predicted price after {num_days} days: {np.mean(average_predected_price_per_simulation)}")
    
    plt.title(f"{ticker} Monte Carlo Simulation ({num_simulation} runs, {num_days} days)")
    plt.xlabel("Days")
    plt.ylabel("Simulated Price")
    plt.show()

    


if __name__ == "__main__":
    ticker = "AAPL"
    num_simulaiton = 1000
    num_days = 252
    monte_carlo_stock_simulation(ticker, num_simulaiton, num_days)