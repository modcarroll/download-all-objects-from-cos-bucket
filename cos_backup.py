import ibm_boto3
from ibm_botocore.client import Config, ClientError
import os
from dotenv import load_dotenv
load_dotenv()

source_apikey = os.getenv("SOURCEAPIKEY")
source_resource_crn = os.getenv("RESOURCECRN")
source_auth_endpoint = os.getenv("AUTHENDPOINT")
source_endpoint = os.getenv("ENDPOINT")
source_bucket_name = os.getenv("BUCKETNAME")

cos = ibm_boto3.resource("s3",
    ibm_api_key_id=source_apikey,
    ibm_service_instance_id=source_resource_crn,
    ibm_auth_endpoint=source_auth_endpoint,
    config=Config(signature_version="oauth"),
    endpoint_url=source_endpoint
)

files = cos.Bucket(source_bucket_name).objects.all()
for file in files:
    try:
        fileName = file.key.replace("/", "-")
        downloadedFile = cos.meta.client.download_file(source_bucket_name, file.key, fileName)
    except Exception as e:
        print("Exception occured: ")
        print(e)
print("Mission accomplished.")
