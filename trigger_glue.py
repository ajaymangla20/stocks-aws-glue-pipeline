
import boto3

def lambda_handler(event, context):
    glue = boto3.client('glue')
    job_name = 'your-glue-job-name'
    
    response = glue.start_job_run(JobName=job_name)
    
    return {
        'statusCode': 200,
        'body': f"Triggered Glue Job: {job_name}, Run ID: {response['JobRunId']}"
    }
