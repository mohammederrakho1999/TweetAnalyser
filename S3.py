import glob
import os
import os.path
import boto3
import configparser
from pathlib import Path

config = configparser.ConfigParser()
config.read_file(open("config.cfg"))

S3 = boto3.client(service_name="s3", region_name="eu-west-1", aws_access_key_id=config.get("AWS", "AWSAccessKeyId"),
                  aws_secret_access_key=config.get("AWS", "AWSSecretKey"))


def upload_to_bucket():
  FOLDER_NAME = "tweetanalyser/tweetanalyser"
  csv_files = glob.glob(
    "C:/Users/info/Desktop/projects/tweetanalyser/data/*.csv")
  for filename in csv_files:
    key = "%s/%s" % (FOLDER_NAME, os.path.basename(filename))
    print("Putting %s as %s" % (filename, key))
    S3.upload_file(filename, config.get(
        "BUCKET", "bucket_name"), key)
