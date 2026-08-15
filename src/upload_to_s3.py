from s3_utils import upload_file_to_s3


BUCKET_NAME = "customer-churn-aws-lautaro"

LOCAL_FILE = "models/customer_churn_model.pkl"

S3_FILE = "models/customer_churn_model.pkl"


upload_file_to_s3(
    LOCAL_FILE,
    BUCKET_NAME,
    S3_FILE
)