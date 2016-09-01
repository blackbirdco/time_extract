# -*- coding: utf-8 -*-
import sys
import os

sys.path.insert(0, "./lib")

import cherrypy
import yaml
import json

from json_tools import jsonify_error
from SEM import MetadataExtractor

from dictionaries_service import DictionariesService
from grammars_service import GrammarsService

# Cherrypy endpoints

allowed_metadata = [
    'date', 
]
token = os.getenv('NLP_TOKEN', yaml.load(open('secrets/config.yml', 'r'))['token'])
print token

class Metadata(object):
    exposed = True
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()

    def POST(self):
        message = cherrypy.request.json.get('message', None)
        name = cherrypy.request.json.get('name', None)
        auth_token = cherrypy.request.headers.get('Http-Auth', None)

        if auth_token != token:
            raise cherrypy.HTTPError(401, "Unauthorized")
        elif not message:
            raise cherrypy.HTTPError(422, "Message is missing")
        elif not name:
            raise cherrypy.HTTPError(422, "Name is missing")
        elif name not in allowed_metadata:
            raise cherrypy.HTTPError(422, name + " is not an allowed metadata")
        else:
            extractor = MetadataExtractor(message, [name])
            return extractor.perform()

class Stemmer(object):
    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()

    def post(self):
        message = cherrypy.request.json.get('message', None)
        auth_token = cherrypy.request.headers.get('Http-Auth', None)

        if auth_token != token:
            raise cherrypy.HTTPError(401, "Unauthorized")
        elif not message:
            raise cherrypy.HTTPError(422, "Message is missing")
        else:
            stemmer = MessageStemmer(message)
            return stemmer.perform()

# ==================================
# Cherrypy configuration and routing
# ==================================

cherrypy.server.socket_host = '0.0.0.0'
cherrypy.config.update({'/': { 'error_page.default': jsonify_error } })

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')

    DictionariesService().load()
    GrammarsService().load()

    cherrypy.tree.mount(Metadata(), '/api/v1/metadata', 'config/cherrypy.conf')

    cherrypy.engine.start()
    cherrypy.engine.block()
