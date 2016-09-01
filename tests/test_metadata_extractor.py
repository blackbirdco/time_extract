# -*- coding: utf-8 -*-

# Can import from parent directory
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

reload(sys)
sys.setdefaultencoding('utf8')

import unittest
from freezegun import freeze_time

from SEM import MetadataExtractor

@freeze_time("2016-06-30", tz_offset=0)
class MetadataExtractorTest(unittest.TestCase):
    # DO NOT WRITE NEW METADATA TESTS HERE : PICK THE SPECIFIC METADATA TEST FILE

    # Perform without metadata
    def test_perform_with_metadata_to_extract(self):
        self.assertEqual(MetadataExtractor('je veux un petit ricard dans un verre à ballon', ['date']).perform(), {})

    # Perform with metadata
    def test_perform_with_metadata(self):
        self.assertEqual(MetadataExtractor('je veux un petit ricard lundi', ['date']).perform()['timestamp'], 1467590400.0)

    # Perform with two metadata
    # V2

    # Perform with two metadata asked and only one present
    # V2
