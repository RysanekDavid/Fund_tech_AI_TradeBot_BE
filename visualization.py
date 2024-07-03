import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the processed data
df = pd.read_csv("processed_eurusd_data.csv", index_col="Datetime", parse_dates=True)

# Plot price and moving averages
plt.figure(figsize=(12, 6))
plt.plot(df.index, df['Close'], label='Close Price')
plt.plot(df.index, df['SMA_50'], label='50-day SMA')
plt.plot(df.index, df['SMA_200'], label='200-day SMA')
plt.title('EURUSD Price and Moving Averages')
plt.legend()
plt.savefig('price_and_ma.png')
plt.close()

# Plot RSI
plt.figure(figsize=(12, 6))
plt.plot(df.index, df['RSI'])
plt.title('EURUSD RSI')
plt.axhline(y=70, color='r', linestyle='--')
plt.axhline(y=30, color='g', linestyle='--')
plt.savefig('rsi.png')
plt.close()

print("Visualizations saved as price_and_ma.png and rsi.png")