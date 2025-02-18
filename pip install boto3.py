pip install boto3
import boto3

# Initialize S3 client
s3_client = boto3.client('s3')

# Define file details
bucket_name = "your-bucket-name"
file_name = "local-file-path.txt"  # Path to your file
s3_key = "uploaded-file-name.txt"  # Name in S3

# Upload file
s3_client.upload_file(file_name, bucket_name, s3_key)

print(f"File '{file_name}' uploaded to '{bucket_name}/{s3_key}'")

