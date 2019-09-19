import ibm_boto3
from ibm_botocore.client import Config, ClientError

source_apikey = "{api-key}"
source_resource_crn = "{resource-crn}"
source_auth_endpoint = "{auth-endpoint}"
source_endpoint = "{endpoint}"
source_bucket_name = "{bucket-name}"

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
