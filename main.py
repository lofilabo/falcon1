# things.py

# Let's get this party started!
import falcon
import tenjin
from tenjin.helpers import *
import pprint
import json

# Falcon follows the REST architectural style, meaning (among
# other things) that you think in terms of resources and state
# transitions, which map to HTTP verbs.


class ThingsResource(object):
    def on_get(self, req, resp):
        for key, value in req.params.items():
            print (key, "=>", value)

        context = {
            'title': 'Template Example',
            'items': [
                'Line 1',
                'Line 2',
                'Line 3',
                'Line 4',
                'Line 5',
                'Line 6',
            ],

            'rec': {
                "p1": 100,
                "p2": 200,
                "p3": 300,
                "p4": 400,
                "p5": 500,
                "p6": 600
            }

        }
        y = json.dumps(context)
        engine = tenjin.Engine(path=['views'])
        html = engine.render('page.pyhtml', context)
        # print(html)

        resp.status = falcon.HTTP_200  # This is the default status
        #resp.content_type = 'text/html'

        resp.body = (y)
        #resp.body = (html)
        #resp.body = ('<h2>I Want Your...BRAINS.</h2><h4>Brains. Brains. Brains.</h4>')


class ThingsResourceArg(object):
    def on_get(self, req, resp, arg):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200  # This is the default status
        resp.content_type = 'text/html'
        resp.body = ('\n<p>' + arg + '</p>')


class ThingsResource2Arg(object):
    def on_get(self, req, resp, arg1, arg2):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200  # This is the default status
        resp.content_type = 'text/html'
        resp.body = ('<h1>GET</h1><p>' + arg1 + '</p>' + '<p>' + arg2 + '</p>')

    def on_post(self, req, resp, arg1, arg2):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200  # This is the default status
        resp.content_type = 'text/html'
        resp.body = ('<h1>POST</h1><p>' + arg1 +
                     '</p>' + '<p>' + arg2 + '</p>')



# falcon.API instances are callable WSGI apps
app = falcon.API()

# Resources are represented by long-lived class instances
things = ThingsResource()
things_arg = ThingsResourceArg()  # resource for route: '/things/{arg}'
# resource for route: '/things/thing/{arg1}/{arg2}'
things_2arg = ThingsResource2Arg()

# things will handle all requests to the '/things' URL path
app.add_route('/things', things)

# for reference - how to add longer and more complex routes
app.add_route('/things/{arg}', things_arg)  # with and argument
app.add_route('/things/thing/{arg1}/{arg2}', things_2arg)  # with 2 arguments!!
# please see note "MORE COMPLEX ROUTES" above.
