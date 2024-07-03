import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

# Calculate the start date (730 days ago)
end_date = datetime.now()
start_date = end_date - timedelta(days=730)

# Fetch EURUSD data
eurusd = yf.Ticker("EURUSD=X")
df = eurusd.history(start=start_date, end=end_date, interval="1h")

# Save to CSV
df.to_csv("eurusd_data.csv")

print(df.head())
print(f"Data shape: {df.shape}")