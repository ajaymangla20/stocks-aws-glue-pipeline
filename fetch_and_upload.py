
import yfinance as yf
import boto3
from io import StringIO
from datetime import datetime

# Configs
TICKER = "AAPL"
BUCKET = "your-bucket-name"
PREFIX = "raw-stock-data/"

# Download data
df = yf.download(TICKER, period="7d", interval="1d")
csv_buffer = StringIO()
df.to_csv(csv_buffer)

# Upload to S3
s3 = boto3.client('s3')
key = f"{PREFIX}{TICKER}_{datetime.now().date()}.csv"
s3.put_object(Bucket=BUCKET, Key=key, Body=csv_buffer.getvalue())

print(f"Uploaded {key} to S3 bucket {BUCKET}")
