# -*- coding: utf-8 -*-
import os
import os.path
import re

multiword_expressions = {}

class MultiwordExpressionsService:
    def load(self):
        global multiword_expressions
        if multiword_expressions == {}:
            print "Loading multiword expressions"
                
            with open('./config/data/MWE_fr.dic', 'rb') as mwe_file:
                mwe_list = mwe_file.readlines()
                mwe_list = map(lambda s: s.strip(), mwe_list)
                for expression in mwe_list:
                    sanitized_expression = expression.replace(" ", "_")
                    multiword_expressions[expression] = sanitized_expression

        return multiword_expressions
