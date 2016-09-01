# -*- coding: utf-8 -*-

import os
import os.path
import re
import nltk
from nltk.parse import RecursiveDescentParser

from StringIO import StringIO

grammars = {}

class GrammarsService:
    def load(self):
        global grammars

        if grammars == {}:
            for file in os.listdir('./grammars'):
                with open('./grammars/' + file, 'r+') as grammar_file :
                    metadata_name = re.sub(r'.txt', r'', file)
                    temporary_gammar = StringIO()
                    temporary_gammar.write('')

                    for line in grammar_file :
                        temporary_gammar.write(line)

                    CFGgrammar = nltk.CFG.fromstring(temporary_gammar.getvalue())
                    rd_parser = nltk.RecursiveDescentParser(CFGgrammar)

                    grammars[metadata_name] = rd_parser
                    print "Loading parser from %s grammar" % metadata_name

        return grammars


