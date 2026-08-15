import boto3

def upload_file_to_s3(local_file, bucket_name, s3_file):
    """
    Uploads a file to an S3 bucket.
    Parameters
    ----------
    local_file : str
        Path to the local file.
    bucket_name : str
        Name of the S3 bucket.
    s3_file : str
        Name/path of the file in S3.
    """
    s3 = boto3.client('s3')

    s3.upload_file(local_file, bucket_name, s3_file)

    print(f"Uploaded {local_file} to s3://{bucket_name}/{s3_file}")

