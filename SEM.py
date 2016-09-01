# -*- coding: utf-8 -*-
import sys

sys.path.insert(0, "./lib")

from dictionaries_service import DictionariesService
from grammars_service import GrammarsService
from tree_tagger_wrapper import TreeTaggerWrapper
from translate_to_json_service import TranslateToJsonService

class MetadataExtractor:
    def __init__(self, message, *args):
        self.message = message
        self.metadata = args[0][0]
        self.args = args

    def perform(self):
        ''' La fonction prend comme paramètres un message de type string et une liste de metadata.

            Le message est écrit dans un fichier texte pris comme input pour TreeTagger.
            La sortie de TreeTagger est un fichier csv en 3 colonnes (wordForm, POS, lemma).
            Les lemmas du fichier csv sont comparés avec les lemmas du dictionnaire de concepts (reconnus par la grammaire).

            La fonction ouvre les fichiers grammaires correspondants aux metadatas en paramètres.
            Les grammaires sont mergées dans une grammaire temporaire à passer comme input au parser sémantique.

            Le parser sémantique repose sur une grammaire CFG (Context Free Grammar). Le parser sort un arbre d'analyse.
            En dernière étape, cet arbre est transformé en JSON arborescent.
        '''

        message_tags = TreeTaggerWrapper().parse(self.message)
        print "Extracted treetagger :\n%s\n" % message_tags

        extracted_lemma_list = self.extract_lemma(message_tags)
        print "Pertinent lemma :\n%s\n" % extracted_lemma_list

        parsing = self.parse_semantic_from(extracted_lemma_list)
        print "Parsed semantic :\n%s\n" % parsing

        return TranslateToJsonService(self.metadata, parsing).perform()

    def extract_lemma(self, message_tags):
        dictionaries = DictionariesService().load()
        dictionary = dictionaries[self.metadata]

        lemmas = []
        for tag in message_tags:
            if any(dic.concept == tag.lemma for dic in dictionary):
                lemmas.append(tag.lemma)

        return lemmas

    def parse_semantic_from(self, extracted_lemmas):
        grammar = GrammarsService().load()
        parsing = None

        for tree in grammar[self.metadata].parse(extracted_lemmas):
            parsing = tree

        return parsing

if __name__ == "__main__":
    reload(sys)
    sys.setdefaultencoding('utf8')

    listArg = sys.argv
    message = listArg[1]
    metadata = listArg[2:]

    klass = MetadataExtractor(message, metadata)
    print klass.perform()
