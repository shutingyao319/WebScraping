import yfinance as yf
import pandas as pd

shopify = yf.Ticker("Shop")
shopify_data = shopify.history(period="max")
shopify_data.reset_index(inplace=True)
shopify_data.head()
print(shopify_data)