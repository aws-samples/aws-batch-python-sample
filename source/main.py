import argparse
import logging
import sys

from awsS3Io import AwsS3Io
from sampleProcess import SampleProcess


def run(output_dir, s3destination):
    downloaded_file = SampleProcess().run(output_dir)
    # If s3 uri is present upload to s3
    if s3destination is not None:
        AwsS3Io().uploadfile(downloaded_file, s3destination)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("output_dir",
                        help="The output location to save the data to")

    parser.add_argument("--s3uri",
                        help="This is optional, provide the path if you want to upload the data to s3", default=None)

    parser.add_argument("--log-level", help="Log level", default="INFO", choices={"INFO", "WARN", "DEBUG", "ERROR"})

    args = parser.parse_args()

    # Set up logging
    logging.basicConfig(level=logging.getLevelName(args.log_level), handlers=[logging.StreamHandler(sys.stdout)],
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)

    # Start process
    logger.info("Starting run with arguments...\n{}".format(args.__dict__))

    run(args.output_dir, args.s3uri)

    logger.info("Completed run...")
