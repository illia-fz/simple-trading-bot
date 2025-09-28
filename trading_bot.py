import random


def generate_prices(n=50, start=100.0):
    """Generate a list of simulated price data."""
    prices = [start]
    for _ in range(n - 1):
        change = random.uniform(-2, 2)
        prices.append(max(0.1, prices[-1] + change))
    return prices


def moving_average(data, window):
    """Calculate simple moving average for each point."""
    ma = []
    for i in range(len(data)):
        if i + 1 < window:
            ma.append(sum(data[: i + 1]) / (i + 1))
        else:
            window_data = data[i - window + 1 : i + 1]
            ma.append(sum(window_data) / window)
    return ma


def simulate_bot():
    """Simulate a simple moving average crossover trading bot."""
    prices = generate_prices(50)
    ma_short = moving_average(prices, 5)
    ma_long = moving_average(prices, 15)
    for price, short, long in zip(prices, ma_short, ma_long):
        action = "BUY" if short > long else "SELL"
        print(
            f"Price: {price:.2f}, MA5: {short:.2f}, MA15: {long:.2f} -> {action}"
        )


if __name__ == "__main__":
    simulate_bot()
