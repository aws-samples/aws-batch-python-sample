import logging
import os
import urllib.request

"""
This is a simple sample that downloads a json formatted address and writes the output to a directory
"""


class SampleProcess:
    def __init__(self, uri="http://maps.googleapis.com/maps/api/geocode/json?address=google"):
        self.uri = uri

    @property
    def logger(self):
        return logging.getLogger(__name__)

    def run(self, output_dir):
        output_filename = os.path.join(output_dir, "sample.json")
        self.logger.info("Downloading from {} to {}".format(self.uri, output_filename))

        with urllib.request.urlopen(self.uri) as url:
            data = url.read().decode()

        self.logger.debug("Writing {} to {}", data, output_filename)
        with open(output_filename, "w") as out:
            out.write(data)

        self.logger.info("Download complete..")
        return output_filename
