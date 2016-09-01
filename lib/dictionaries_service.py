# -*- coding: utf-8 -*-
import os
import os.path
import unicodecsv
from collections import namedtuple
import re

dictionaries = {}

class DictionariesService:
    def load(self):
        global dictionaries
        if dictionaries == {}:
            for file in os.listdir('./dictionaries'):
                metadata_name = re.sub(r'.dic', r'', file)
                print "Loading dictionary for %s" % metadata_name
                
                with open('./dictionaries/' + file, 'rb') as concepts_dictionary:
                    Tag = namedtuple('Tag', 'concept, pos, semanticType')
                    dictionary = []
                    for tag in map(Tag._make, unicodecsv.reader(concepts_dictionary, delimiter='\t', encoding='utf-8')):
                        dictionary.append(tag)

                    dictionaries[metadata_name] = dictionary
                    
        return dictionaries

