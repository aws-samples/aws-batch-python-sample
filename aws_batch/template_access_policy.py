from urllib.parse import urlparse


def create_access_policy(s3_bucket_uri):
    """
This is the policy required to run this sample job
    :param s3_bucket_uri: The s3 bucket path to put the results to
    :return: The access policy json
    """

    parsed_url = urlparse(s3_bucket_uri)

    bucket_name = parsed_url.netloc
    key = parsed_url.path

    # This is custom for the batch
    access_policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "BucketKeyAccess",
                "Effect": "Allow",
                "Action": [
                    "s3:PutObject",
                    "s3:GetObject",
                    "s3:DeleteObject",

                ],
                "Resource": [
                    "arn:aws:s3:::{}{}*".format(bucket_name, key),
                ]
            },
            {
                "Sid": "BuckeyAccess",
                "Effect": "Allow",
                "Action": [
                    "s3:ListBucket",
                    "s3:HeadBucket"
                ],
                "Resource": [
                    "arn:aws:s3:::{}".format(bucket_name)
                ]
            }
        ]
    }
    return access_policy
