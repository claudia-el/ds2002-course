

import boto3
import os
import sys


def upload_file(bucket, local_file, public=False):

    object_name = os.path.basename(local_file)
    s3 = boto3.client('s3', region_name='us-east-1')


    try:
        s3.put_object(
            Body =open(local_file, 'rb'),
            Bucket=bucket,
            Key=object_name,
            ACL='public-read' if public else 'private'
            )
        return object_name
    except Exception as e:
        print(f"Upload failed: {e}")

def generate_presigned_url(bucket, local_file, exp):
    
    s3 = boto3.client('s3', region_name='us-east-1')
    
    try:
        url = s3.generate_presigned_url(
            'get_object',
            Params={'Bucket': bucket, 'Key': local_file},
            ExpiresIn=int(exp)
        )

        return url

    except Exception as e:
        print(f"Failed to generate presigned URL: {e}")

if __name__ == "__main__":

    bucket = sys.argv[1]
    local_file = sys.argv[2]
    exp = int(sys.argv[3])
    public = sys.argv[4].lower() == 'true'

    object_name = upload_file(bucket, local_file, public)

    if public:
        print(f"Public URL: https://{bucket}.s3.amazonaws.com/{object_name}")
    else:

        print(generate_presigned_url(bucket, local_file, exp))

