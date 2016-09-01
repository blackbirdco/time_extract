import sys
import importlib

from json_renders import *

class TranslateToJsonService:
    def __init__(self, metadata_name, semantic_tree):
        self.semantic_tree = semantic_tree
        self.metadata_name = metadata_name
        self.dictionary = {}

    def perform(self):
        if self.semantic_tree is None:
            return {}
        
        klass = self.metadata_service_class()
        return klass(self.metadata_name, self.semantic_tree).perform()
    
    def metadata_service_class(self):
        class_name = (self.metadata_name+'_render').title().replace('_', '')
        module = 'json_renders.'+self.metadata_name+'_render'
        return reduce(getattr, class_name.split("."), sys.modules[module])
