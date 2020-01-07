import os
import tempfile
from unittest import TestCase

from sampleProcess import SampleProcess

"""
This a integration test
"""


class ITTestSampleProcess(TestCase):

    def test_run(self):
        # Arrange
        sut = SampleProcess()
        tmpout = tempfile.mkdtemp()

        # Act
        actual = sut.run(output_dir=tmpout)

        # Assert
        # Check the file downloaed exits is greater than zero bytes
        self.assertTrue(os.path.getsize(actual) > 0)
