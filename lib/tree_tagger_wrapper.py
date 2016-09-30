# -*- coding: utf-8 -*-
import sys
import atexit
import treetaggerwrapper
import treetaggerpoll
import uuid
import re

from multiword_expressions_service import MultiwordExpressionsService

treetagger_instances = []
current_instance = 0

def clean_treetagger_processes(treetagger_instances):
    if treetagger_instances != []:
        for i in range(2):
            treetagger_instances[i].stop_poll()

class TreeTaggerWrapper():
   
    def generate_treetagger_processes(self):
        global treetagger_instances

        if treetagger_instances == []:
            for i in range(2):
                treetagger_instances.append(treetaggerpoll.TaggerProcessPoll(
                    TAGDIR = '/usr/local', 
                    TAGLANG = 'fr', 
                    TAGOPT = '-no-unknown -token -lemma -sgml -quiet'
                ))
            atexit.register(clean_treetagger_processes, treetagger_instances)

        return treetagger_instances

    def treetagger(self, message):
        global current_instance
        global treetagger_instances
        self.generate_treetagger_processes()

        current_instance = (current_instance + 1) % 2
        tagger = treetagger_instances[current_instance]
        
        message = message.decode('utf-8')
        parsing = tagger.tag_text_async(message)
        parsing.wait_finished()
        
        tags = treetaggerwrapper.make_tags(parsing.result)
        return tags

    def kept_words(self):
        return '[0-9]+|mois|été|asap|h|-ce|m2|m²|min|max|rdc|colloc|coloc|start-up|meublé|paris|.*\_'

    def touch_up_results(self, tags):
        for i in range(len(tags)):
            word = tags[i].word
            
            if re.match(self.kept_words(), word): 
                tags[i] = tags[i]._replace(lemma = word)
    
        return tags

    def parse(self, message):
        message = self.prepare_message_for_tree_tagger(message)
        message = self.sanitize_multiword_expressions(message)
        treetagger_output = self.treetagger(message)
        corrected_results = self.touch_up_results(treetagger_output)
      
        return corrected_results

    def sanitize_multiword_expressions(self, message):
        mwe = MultiwordExpressionsService().load()
        sanitized_message = message

        for expression, sanitized_expression in mwe.items():
            if expression in sanitized_message:
                sanitized_message = sanitized_message.replace(expression, sanitized_expression)

        return sanitized_message
        # multiword_expressions = regexp_tokenize(new_message, pattern='\S+')
        # multiword_expressions = ' '.join(multiword_expressions)

    def prepare_message_for_tree_tagger(self, message):
        content = message.lower()
        replace = re.sub(r'([0-9]+)(janvier|février|fevrier|mars|avril|mai|juin|juillet|août|aout|septembre|octobre|novembre|décembre|decembre)', r'\1 \2', content)
        replace = re.sub(r'([0-9]+)(m2|m|h|j|jour|jours|mois|semaine|semaines|semestre|semestres|an|ans)', r' \1 \2 ', replace)
        replace = re.sub(r'([0-9]+)([:.])([0-9]+)', r'\1 h \3', replace)
        replace = re.sub(r'(/)', r' \1 ', replace)
        replace = re.sub(r'(\.)', r' \1 ', replace)
        replace = re.sub(r'(\-)', r' \1 ', replace)
        replace = re.sub(r'([0-9]+)(-)([0-9]+)', r' \1 \2 \3', replace)
        replace = re.sub(r'(d)(un|une)', r' \1 \2 ', replace)

        return replace
