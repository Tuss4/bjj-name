import falcon
import json
import logging
import sys
from app.bjj_name import get_last_name, update_first_name


api = application = falcon.API()


class PingResource(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = ('Ping yo.')


class NameResource(object):

    def __init__(self):
        self.logger = logging.getLogger('bjjnameapp.' + __name__)

    def on_post(self, req, resp):
        body = json.loads(req.stream.read())
        resp.status = falcon.HTTP_201
        first_name = update_first_name(body['first_name'])
        last_name = get_last_name()
        new_name = first_name + " " + last_name
        resp.body = (json.dumps({"bjj_name": new_name}))


ping = PingResource()
new_name = NameResource()

api.add_route('/', ping)
api.add_route('/name', new_name)