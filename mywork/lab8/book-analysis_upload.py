import argparse
import glob
import logging
import os
import boto3

logger = logging.getLogger()
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def parse_args():
    """Parses command line arguments"""

    parser = argparse.ArgumentParser()

    parser.add_argument("input_folder", type=str)
    parser.add_argument("destination", type=str)
    args = parser.parse_args()

    return args.input_folder, args.destination

def upload(input_folder, destination):
    """Uploads files under specified prefix to s3 bucket"""
    
    bucket, prefix = destination.split("/", 1)

    try:
        s3 = boto3.client("s3")
        for file_path in glob.glob(os.path.join(input_folder, "results*.csv")):
            key = prefix + os.path.basename(file_path)
            s3.upload_file(file_path, bucket, key)
    except Exception as e:
        logger.error(e)


if __name__ == "__main__":

    logging.basicConfig(level=logging.INFO)

    input_folder, destination = parse_args()
    upload(input_folder, destination)
    logger.info("Upload complete.")


