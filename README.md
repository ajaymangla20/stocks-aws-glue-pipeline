
# 🧠 yfinance Stock ETL Pipeline on AWS

An end-to-end AWS pipeline to fetch stock data using yfinance, store in S3, trigger an SNS event, run a Lambda to start a Glue ETL job.

## 💡 Stack
- Python (yfinance, boto3)
- AWS S3, SNS, Lambda, Glue
- Optional: Terraform

## 🚀 Flow
1. Run `fetch_and_upload.py` to download and push data to S3.
2. S3 event triggers SNS → Lambda.
3. Lambda starts Glue Job.
4. Glue job cleans and writes processed data to S3.



