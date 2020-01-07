import logging
import os

import boto3

"""
S3 upload download operations
"""


class AwsS3Io:

    def __init__(self):
        self.client = None

    @property
    def logger(self):
        return logging.getLogger(__name__)

    @property
    def client(self):
        self.__client__ = self.__client__ or boto3.resource('s3').meta.client
        return self.__client__

    @client.setter
    def client(self, value):
        self.__client__ = value

    def uploadfile(self, localpath, s3path):
        """
Uploads a file to s3
        :param localpath: The local path
        :param s3path: The s3 path in format s3://mybucket/mydir/mysample.txt
        """
        self.logger.info("Upload file {} to s3 {}".format(localpath, s3path))

        bucket, key = self.get_bucketname_key(s3path)

        if key.endswith("/"):
            key = "{}{}".format(key, os.path.basename(localpath))

        self.client.upload_file(localpath, bucket, key)

    def get_bucketname_key(self, uripath):
        assert uripath.startswith("s3://")

        path_without_scheme = uripath[5:]
        bucket_end_index = path_without_scheme.find("/")

        bucket_name = path_without_scheme
        key = "/"
        if bucket_end_index > -1:
            bucket_name = path_without_scheme[0:bucket_end_index]
            key = path_without_scheme[bucket_end_index + 1:]

        return bucket_name, key
