import os
import boto3
from botocore import UNSIGNED
from botocore.config import Config

def download_s3_folder(bucket_name, s3_folder, local_dir):
    """
    Download the contents of a folder directory
    Args:
    - bucket_name : String
    - s3_folder   : String
    - local_dir   : String
    """
    # Create a boto3 client with unsigned config
    s3 = boto3.client('s3', config=Config(signature_version=UNSIGNED))

    try:
        paginator = s3.get_paginator('list_objects')
        for page in paginator.paginate(Bucket=bucket_name, Prefix=s3_folder):
            if "Contents" in page:
                for obj in page["Contents"]:
                    key = obj['Key']
                    if not key.endswith('/'):  # skip directories
                        # Create a local path relative to the s3_folder
                        local_file_path = os.path.join(local_dir, os.path.relpath(key, s3_folder))
                        
                        # Ensure local directory exists
                        local_file_dir = os.path.dirname(local_file_path)
                        if not os.path.exists(local_file_dir):
                            os.makedirs(local_file_dir)
                        
                        # Download file
                        s3.download_file(bucket_name, key, local_file_path)
                        print(f"Downloaded {key} to {local_file_path}")
    except KeyError:
        print(f"No objects found in {bucket_name}/{s3_folder}")

bucket = 'oedi-data-lake'
base_s3_path = 'PR100/'

# Local base path
local_base_path = './PR100_new'

download_s3_folder(bucket, base_s3_path, local_base_path)

print("Data download complete.")
