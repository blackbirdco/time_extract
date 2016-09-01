# -*- coding: utf-8 -*-

import cherrypy
import json

def jsonify_error(status, message, traceback, version):
    response = cherrypy.response
    response.headers['Content-Type'] = 'application/json'

    return json.dumps({'status': int(status.split()[0]), 'message': message})
