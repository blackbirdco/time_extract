# -*- coding: utf-8 -*-

import time
import datetime as dt
from datetime import date
from datetime import datetime as dt
from datetime import timedelta
from datetime import time
from time import mktime
import dateparser

class DateRender:
    def __init__(self, metadata_name, tree):
        self.tree = tree
        self.metadata_name = metadata_name
        self.dictionary = {}

    def perform(self):
        return self.to_i([self.metadata_name])

    def metadata_text(self, subtree):
        self.dictionary['text'] = ' '.join(subtree.leaves())

    def today(self, subtree):
        currentTime = dt.today()
        currentTimestamp = mktime(currentTime.timetuple())
        self.dictionary['timestamp'] = currentTimestamp

    def tommorow(self, subtree):
        dayAfterTime = dt.today() + timedelta(days=1)
        dayAfterTimestamp = mktime(dayAfterTime.timetuple())
        self.dictionary['timestamp'] = dayAfterTimestamp

    def yesterday(self, subtree):
        day_before_time = dt.today() + timedelta(days=-1)
        day_before_timestamp = mktime(day_before_time.timetuple())
        self.dictionary['timestamp'] = day_before_timestamp
        
    def nth_day_of_week(self, subtree):
        if subtree.label().startswith('first'):
            n = 0
        if subtree.label().startswith('second'):
            n = 1
        if subtree.label().startswith('third'):
            n = 2
        if subtree.label().startswith('fourth'):
            n = 3
        if subtree.label().startswith('fifth'):
            n = 4
        if subtree.label().startswith('sixth'):
            n = 5
        if subtree.label().startswith('seventh'):
            n = 6

        d = dt.today()
        self.dictionary['timestamp'] = self.next_weekday(d, n)

    def noon(self, subtree):
        if('timestamp' not in self.dictionary):
            self.dictionary['timestamp'] = mktime(dt.today().timetuple())
        self.dictionary['timestamp'] += 12 * 3600
        self.dictionary['hours'] = '12'

    def midnight(self, subtree):
        if('timestamp' not in self.dictionary):
            self.dictionary['timestamp'] = mktime(dt.today().timetuple())
        self.dictionary['timestamp'] += 24 * 3600
        
    def next_weekday(self, d, weekday):
        days_ahead = weekday - d.weekday()
        if days_ahead <= 0: # Target day already happened this week
            days_ahead += 7
        return mktime((d + timedelta(days_ahead)).timetuple())

    def to_i(self, arg):
        for subtree in self.tree.subtrees():
            if subtree.label() == 'metadata':
                self.metadata_text(subtree)

            if subtree.label()[:-4] == self.metadata_name:
                self.dictionary['metadata'] = self.metadata_name

            if subtree.label() == 'todayItem':
                self.today(subtree)

            if subtree.label() == 'tomorrowItem':
                self.tommorow(subtree)

            if subtree.label() == 'yesterdayItem':
                self.yesterday(subtree)

            if subtree.label() == 'middayItem':
                self.noon(subtree)

            if subtree.label() == 'midnightItem':
                self.midnight(subtree)

            if 'DayOfWeekItem' in subtree.label():
                self.nth_day_of_week(subtree)

            if subtree.label() == 'dayValueItem':
                self.dictionary['day'] = ' '.join(subtree.leaves())

            if subtree.label() == 'monthValueItem':
                self.dictionary['month'] = ' '.join(subtree.leaves())
        
        if (('day' in self.dictionary) or ('month' in self.dictionary)):
            dateStr = ''
            if ('day' in self.dictionary):
                dateStr += self.dictionary['day'] + ' ' 
            if ('month' in self.dictionary):
                dateStr += self.dictionary['month'] + ' '
            dateParser = dateparser.parse(dateStr)
            dateTimestamp =  mktime(dateParser.timetuple())
            self.dictionary['timestamp'] = dateTimestamp
            if ('hours' in self.dictionary):
                self.dictionary['timestamp'] += int(self.dictionary['hours']) * 3600
        return self.dictionary
   
