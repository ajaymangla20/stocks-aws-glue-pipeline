
import sys
from awsglue.context import GlueContext
from pyspark.context import SparkContext
from awsglue.utils import getResolvedOptions

args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

# Read data from S3
input_path = "s3://your-bucket-name/raw-stock-data/"
df = spark.read.csv(input_path, header=True, inferSchema=True)

# Basic clean
df_clean = df.filter("Close IS NOT NULL")

# Write to S3 in Parquet format
output_path = "s3://your-bucket-name/processed-stock-data/"
df_clean.write.mode("overwrite").parquet(output_path)
