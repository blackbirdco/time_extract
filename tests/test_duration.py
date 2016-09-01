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

@freeze_time("2016-06-17", tz_offset=0)
class MetadataExtractorTest(unittest.TestCase):
    def test_duration_continous(self):
        return 1
        #self.assertEqual(MetadataExtractor('Je dois trouver un stagiaire asap pour 6 mois intéressé par le conseil et les startups', ['duration']).perform()['timestamp'], 1467158400.0)

    def test_duration_continous_half(self):
        return 1
        #self.assertEqual(MetadataExtractor('1 mois et demi en Irlande ou en angleterre avec un budget de 1500', ['duration']).perform()['timestamp'], 1467158400.0)

    def test_duration_limited_interval(self):
        return 1
        #self.assertEqual(MetadataExtractor('tu as pas une petite rando en Ardèche d\'une durée de 6 - 7 jours entre pote', ['duration']).perform()['timestamp'], 1467158400.0)

    def test_duration_min_limited_interval(self):
        return 1
        #self.assertEqual(MetadataExtractor('Je dois trouver un stage asap pour plus de 6 mois', ['duration']).perform()['timestamp'], 1467158400.0)
        #self.assertEqual(MetadataExtractor('Je dois trouver un stage asap au min de 6 mois', ['duration']).perform()['timestamp'], 1467158400.0)

    def test_duration_approximative(self):
        return 1
        #self.assertEqual(MetadataExtractor('Je dois trouver un stage asap d\'environ 6 mois', ['duration']).perform()['timestamp'], 1467158400.0)


