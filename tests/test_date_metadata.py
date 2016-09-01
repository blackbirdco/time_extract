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
    # Common
    def test_without_metadata_to_extract(self):
        self.assertEqual(MetadataExtractor('je veux un petit ricard dans un verre à ballon', ['date']).perform(), {})

    # Datetime
    def test_date_next_day(self):
        self.assertEqual(MetadataExtractor('je veux partir lundi', ['date']).perform()['timestamp'], 1467590400.0)

    def test_date_date_day_month(self):
        self.assertEqual(MetadataExtractor('je cherche du poisson pourri pour le 25 décembre', ['date']).perform()['timestamp'], 1482624000.0)

    def test_date_month(self):
        return 1
        #FIXME make this work
        #self.assertEqual(MetadataExtractor('je cherche des amandes pour décembre', ['date']).perform()['timestamp'], 1480546800.0)

    def test_date_tuesday_noon(self):
        self.assertEqual(MetadataExtractor('je cherche du chocolat pour le mardi midi', ['date']).perform()['timestamp'], 1467720000.0)

    def test_date_22_decembre_noon(self):
        self.assertEqual(MetadataExtractor('je cherche des cacahuètes pour le 22 décembre à midi', ['date']).perform()['timestamp'], 1482408000.0)

    def test_date_calendar_date_day(self):
        self.assertEqual(MetadataExtractor('il y a quoi au ciné le 2 ?', ['date']).perform()['timestamp'], 1464825600.0)
        
    def test_date_calendar_date_day_month(self):
        self.assertEqual(MetadataExtractor('il y a quoi au ciné le 2 juillet ?', ['date']).perform()['timestamp'], 1467417600.0)
        
    def test_date_calendar_date_day_month_year(self):
        self.assertEqual(MetadataExtractor('il y a quoi au ciné le 2 juillet 2016 ?', ['date']).perform()['timestamp'], 1467417600.0)
        
    def test_date_calendar_date_day_of_week_day(self):
        self.assertEqual(MetadataExtractor('il y a quoi au ciné lundi 2 ?', ['date']).perform()['timestamp'], 1464825600.0)
        
    def test_date_calendar_date_day_of_week_day_month(self):
        self.assertEqual(MetadataExtractor('il y a quoi au ciné lundi 2 juin ?', ['date']).perform()['timestamp'], 1464825600.0)
        
    def test_date_calendar_date_day_of_week_day_month_year(self):
        self.assertEqual(MetadataExtractor('il y a quoi au ciné lundi 2 juin 2016 ?', ['date']).perform()['timestamp'], 1464825600.0)

    def test_date_calendar_date_ordinal_day_of_week(self):
        self.assertEqual(MetadataExtractor('il y a quoi au ciné le deuxième vendredi de juillet', ['date']).perform()['timestamp'], 1469836800.0)
        
    def test_date_calendar_date_ordinal_day_of_week_year(self):
        self.assertEqual(MetadataExtractor('il y a quoi au ciné le deuxième vendredi de juillet 2016', ['date']).perform()['timestamp'], 1469836800.0)

    def test_date_day_of_week(self):
        self.assertEqual(MetadataExtractor('il y a quoi au ciné lundi ?', ['date']).perform()['timestamp'], 1467590400.0)

    def test_date_day_of_week_next(self):
        self.assertEqual(MetadataExtractor('il y a quoi au ciné lundi prochain ?', ['date']).perform()['timestamp'], 1467590400.0)

    def test_date_tomorrow(self):
        self.assertEqual(MetadataExtractor('il y a quoi au ciné demain ?', ['date']).perform()['timestamp'], 1467331200.0)

    def test_date_today(self):
        self.assertEqual(MetadataExtractor('il y a quoi au ciné aujourd\'hui ?', ['date']).perform()['timestamp'], 1467244800.0)
    
    def test_date_day_after_tomorrow(self):
        return 1
        #self.assertEqual(MetadataExtractor('il y a quoi au ciné après-demain ?', ['date']).perform()['timestamp'], 1467511200.0)
    
    def test_date_yesterday(self):
        self.assertEqual(MetadataExtractor('il y avait quoi au ciné hier ?', ['date']).perform()['timestamp'], 1467158400.0)

    def test_date_wrong_syntax(self):
        self.assertEqual(MetadataExtractor('il y a quoi au ciné lundi 2juin ?', ['date']).perform()['timestamp'], 1464825600.0)

    def test_date_real_jam_use_case(self):
        return 1
        #self.assertEqual(MetadataExtractor('Salut sais tu quels événements son prévus autour de Montpellier pour le 2 mars 2016', ['date']).perform()['timestamp'], '0')

    def test_date_shortened_date(self):
        return 1
        #self.assertEqual(MetadataExtractor('il y a quoi au ciné le 02/06/2016 ?', ['date']).perform()['timestamp'], 1464825600.0)

    def test_date_absolute_feast(self):
        return 1
        #self.assertEqual(MetadataExtractor('il y a quoi au ciné à Noël ?', ['date']).perform()['timestamp'], 1482631200.0)
        #self.assertEqual(MetadataExtractor('il y a quoi au ciné à Noël 2016 ?', ['date']).perform()['timestamp'], 1482631200.0)

    def test_date_relative_feast(self):
        return 1
        #self.assertEqual(MetadataExtractor('il y a quoi au ciné à Pâques ?', ['date']).perform()['timestamp'], 1492308000.0)
        #self.assertEqual(MetadataExtractor('il y a quoi au ciné à Pâques 2017 ?', ['date']).perform()['timestamp'], 1492308000.0)

    def test_date_event(self):
        return 1
        #self.assertEqual(MetadataExtractor('il y a quoi au ciné à la rentrée ?', ['date']).perform()['timestamp'], 1472695200.0)

    def test_date_before_date(self):
        return 1
        #self.assertEqual(MetadataExtractor('il y a quoi au ciné avant lundi ?', ['date']).perform()['timestamp'], 1472695200.0)

    def test_date_after_date(self):
        return 1
        #self.assertEqual(MetadataExtractor('il y a quoi au ciné après lundi ?', ['date']).perform()['timestamp'], 1472695200.0)

    def test_date_approximative_date(self):
        return 1
        #self.assertEqual(MetadataExtractor('il y a quoi au ciné vers le 2 ?', ['date']).perform()['timestamp'], 1472695200.0)

    def test_date_negative_date(self):
        return 1
        #self.assertEqual(MetadataExtractor('je voudrais un boulot mais sauf le 2', ['date']).perform()['timestamp'], 1472695200.0)

    def test_date_constraint_date(self):
        return 1
        #self.assertEqual(MetadataExtractor('je voudrais un boulot uniquement le 2', ['date']).perform()['timestamp'], 1472695200.0)

    def test_date_vector_date(self):
        return 1
        #self.assertEqual(MetadataExtractor('il y a quoi au ciné dans 2 jours ?', ['date']).perform()['timestamp'], 1472868000.0)
        #self.assertEqual(MetadataExtractor('il y a quoi au ciné dans 2 semaines ?', ['date']).perform()['timestamp'], 1472695200.0)
        #self.assertEqual(MetadataExtractor('il y a quoi au ciné dans 2 mois ?', ['date']).perform()['timestamp'], 1472695200.0)
        #self.assertEqual(MetadataExtractor('il y a quoi au ciné dans 2 ans ?', ['date']).perform()['timestamp'], 1472695200.0)

    def test_date_urgency_date(self):
        return 1
        #self.assertEqual(MetadataExtractor('j'ai besoin d'un job maintenant', ['date']).perform()['timestamp'], 1472695200.0)

    def test_date_indeterminate_date(self):
        return 1
        #self.assertEqual(MetadataExtractor('j'ai besoin d'un job mais je ne sais pas quand', ['date']).perform()['timestamp'], 1472695200.0)

    def test_date_hour(self):
        return 1
        #self.assertEqual(MetadataExtractor('il y a quoi au ciné à 14 heure', ['date']).perform()['timestamp'], 1472695200.0)
        #self.assertEqual(MetadataExtractor('il y a quoi au ciné à 14 heure 30', ['date']).perform()['timestamp'], 1472695200.0)
        #self.assertEqual(MetadataExtractor('il y a quoi au ciné à deux heures', ['date']).perform()['timestamp'], 1472695200.0)
        #self.assertEqual(MetadataExtractor('il y a quoi au ciné au déjeuner', ['date']).perform()['timestamp'], 1472695200.0)
        #self.assertEqual(MetadataExtractor('il y a quoi au ciné à midi', ['date']).perform()['timestamp'], 1472695200.0)
        #self.assertEqual(MetadataExtractor('il y a quoi au ciné à midi et demi', ['date']).perform()['timestamp'], 1472695200.0)
        #self.assertEqual(MetadataExtractor('il y a quoi au ciné à cet après-midi', ['date']).perform()['timestamp'], 1472695200.0)
        #self.assertEqual(MetadataExtractor('il y a quoi au ciné en début de soirée', ['date']).perform()['timestamp'], 1472695200.0)
        #self.assertEqual(MetadataExtractor('il y a quoi au ciné en deuxième partie de soirée', ['date']).perform()['timestamp'], 1472695200.0)

    def test_date_before_hour(self):
        return 1
        #self.assertEqual(MetadataExtractor('il y a quoi au ciné avant 14 heure', ['date']).perform()['timestamp'], 1472695200.0)

    def test_date_after_hour(self):
        return 1
        #self.assertEqual(MetadataExtractor('il y a quoi au ciné après 14 heure', ['date']).perform()['timestamp'], 1472695200.0)

    def test_date_approximative_hour(self):
        return 1
        #self.assertEqual(MetadataExtractor('il y a quoi au ciné vers 14 heure', ['date']).perform()['timestamp'], 1472695200.0)

    def test_date_constraint_hour(self):
        return 1
        #self.assertEqual(MetadataExtractor('il y a quoi au ciné uniquement à 14 heure', ['date']).perform()['timestamp'], 1472695200.0)

    def test_date_vector_hour(self):
        return 1
        #self.assertEqual(MetadataExtractor('il y a quoi au ciné dans 2 heures', ['date']).perform()['timestamp'], 1472695200.0)

    def test_date_date_hour(self):
        return 1
        #self.assertEqual(MetadataExtractor('il y a quoi au ciné lundi à 14 heures', ['date']).perform()['timestamp'], 1472695200.0)
        #self.assertEqual(MetadataExtractor('il y a quoi au ciné à 14 heures lundi', ['date']).perform()['timestamp'], 1472695200.0)

    def test_date_alternative(self):
        return 1
        #self.assertEqual(MetadataExtractor('il y a quoi au ciné lundi ou mardi', ['date']).perform()['timestamp'], 1472695200.0)
        #self.assertEqual(MetadataExtractor('il y a quoi au ciné lundi à 20 heure ou mardi avant 15 heure', ['date']).perform()['timestamp'], 1472695200.0)

    def test_date_group(self):
        return 1
        #self.assertEqual(MetadataExtractor('il y a quoi au ciné lundi et mardi', ['date']).perform()['timestamp'], 1472695200.0)

    def test_date_travel(self):
        return 1
        #self.assertEqual(MetadataExtractor('je voudrais partir à Rome le 3 janvier', ['date']).perform()['timestamp'], 1472695200.0)
        #self.assertEqual(MetadataExtractor('je voudrais partir à Rome le 3 janvier avant 15 heure', ['date']).perform()['timestamp'], 1472695200.0)
        #self.assertEqual(MetadataExtractor('je voudrais revenir à Paris le 3 janvier', ['date']).perform()['timestamp'], 1472695200.0)
        #self.assertEqual(MetadataExtractor('je voudrais partir à Rome le 3 janvier et revenir le 6', ['date']).perform()['timestamp'], 1472695200.0)

