# -*- coding: utf-8 -*-
# Can import from parent directory
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

reload(sys)
sys.setdefaultencoding('utf8')

import unittest
import cherrypy
import json
from cherrypy.test import helper

from json_tools import jsonify_error
from server import Metadata

class NlpServerTest(helper.CPWebCase):
    def setup_server():
        conf = {
            '/': {
                'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
                'error_page.default': jsonify_error,
                'tools.response_headers.headers': [('Content-Type', 'application/json')],
            }
        }
        cherrypy.tree.mount(Metadata(), '/api/v1/metadata', conf)

    setup_server = staticmethod(setup_server)

    def test_happy_path(self):
        payload = { 'message': 'oki', 'name': 'date' }
        token = 'TOKEN'
        content = json.dumps(payload, ensure_ascii=False)
        headers = [['Http-Auth', token], ['Content-Type', 'application/json'], ['Content-Length', str(len(content))]]
        
        self.getPage('/api/v1/metadata', headers, 'POST', content)
        
        self.__http_call(payload, token)
        self.assertStatus('200 OK')

    def test_with_invalid_token(self):
        payload = { 'message': 'oki', 'name': 'date' }
        token = 'invalid'

        self.__http_call(payload, token)
        self.assertStatus('401 Unauthorized')

    def test_without_token(self):
        payload = { 'message': 'oki', 'name': 'date' }
        token = None

        self.__http_call(payload, token)
        self.assertStatus('401 Unauthorized')

    def test_without_message(self):
        payload = { 'name': 'date' }
        token = 'TOKEN'

        self.__http_call(payload, token)
        self.assertStatus('422 ')
        self.assertBody('{"status": 422, "message": "Message is missing"}')

    def test_without_name(self):
        payload = { 'message': 'oki' }
        token = 'TOKEN'

        self.__http_call(payload, token)
        self.assertStatus('422 ')
        self.assertBody('{"status": 422, "message": "Name is missing"}')

    def test_with_invalid_name(self):
        payload = { 'message': 'oki', 'name': 'lol' }
        token = 'TOKEN'

        self.__http_call(payload, token)
        self.assertStatus('422 ')
        self.assertBody('{"status": 422, "message": "lol is not an allowed metadata"}')

    def __http_call(self, payload, token):
        if token is not None:
            headers = self.__headers_with_token(payload, token)
        else:
            headers = self.__default_headers(payload)

        self.getPage('/api/v1/metadata', headers, 'POST', self.__format_payload(payload))

    def __default_headers(self, payload):
        return [['Content-Type', 'application/json'], ['Content-Length', str(len(self.__format_payload(payload)))]]

    def __headers_with_token(self, payload, token):
        return self.__default_headers(payload) + [['Http-Auth', token]]

    def __format_payload(self, payload):
        return json.dumps(payload, ensure_ascii=False)
