from unittest import TestCase
from unittest.mock import Mock

from awsS3Io import AwsS3Io
from ddt import ddt, data, unpack

"""
This is a unit test that mocks boto3 client
"""


@ddt
class TestAwsS3Io(TestCase):

    @data(("mydummyfile", "s3://mockbucket/path", "mockbucket", "path")
        , ("/user/mydummyfile", "s3://mockbucket/path/", "mockbucket", "path/mydummyfile"))
    @unpack
    def test_uploadfile(self, localfile, s3, expected_bucket, expected_key):
        # Arrange
        sut = AwsS3Io()
        mocks3client = Mock()
        sut.client = mocks3client

        # Act
        sut.uploadfile(localfile, s3)

        # Assert s3 client  was called
        mocks3client.upload_file.assert_called_with(localfile, expected_bucket, expected_key)
