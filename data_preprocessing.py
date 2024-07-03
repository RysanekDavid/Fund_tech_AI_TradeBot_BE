import pandas as pd
import numpy as np

def calculate_rsi(prices, window=14):
    delta = prices.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

# Load the data
df = pd.read_csv("eurusd_data.csv", index_col="Datetime", parse_dates=True)

# Convert to UTC
df.index = df.index.tz_localize(None).tz_localize('UTC')

# Remove any rows with missing values
df.dropna(inplace=True)

# Calculate returns
df['Returns'] = df['Close'].pct_change()

# Calculate some basic technical indicators
df['SMA_50'] = df['Close'].rolling(window=50).mean()
df['SMA_200'] = df['Close'].rolling(window=200).mean()
df['RSI'] = calculate_rsi(df['Close'], window=14)

# Remove rows with NaN values that result from indicator calculations
df.dropna(inplace=True)

print(df.head())
print(f"Processed data shape: {df.shape}")

# Save processed data
df.to_csv("processed_eurusd_data.csv")