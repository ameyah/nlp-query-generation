from BaseHTTPServer import BaseHTTPRequestHandler
import json
from controllers import Controllers
from include import utils
import MySQLdb


def HTTPRequestHandlerContainer():

    controller = Controllers()

    class HTTPRequestHandler(BaseHTTPRequestHandler):

        def __init__(self, request, client_address, server):
            BaseHTTPRequestHandler.__init__(self, request, client_address, server)

        # handle POST command
        def do_POST(self):
            print self.path
            if "/preferences" in self.path:
                postvars = utils.get_post_data(self.headers, self.rfile)
                if postvars != '':
                    priorities = None
                    try:
                        for key in postvars:
                            priorities = json.loads(key)
                    except TypeError as e:
                        self.send_bad_request_response()
                    if priorities:
                        pass

                    # result = controller.insert_prestudy_answers(postvars)
                    self.send_ok_response()
                else:
                    self.send_bad_request_response()

        # handle GET command
        def do_GET(self):
            try:
                if "/online" in self.path:
                    self.send_ok_response(data=1)
                else:
                    self.send_bad_request_response()
            except MySQLdb.Error as e:
                print e
                print "exception"

            return

        def send_ok_response(self, **kwargs):
            # send code 200 response
            self.send_response(200)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            if kwargs.get("data"):
                self.wfile.write(kwargs.get("data"))

        def send_bad_request_response(self):
            # send code 200 response
            self.send_response(400)
            self.send_header('Access-Control-Allow-Origin', '*')

        # suppress logs
        def log_message(self, format, *args):
            return

    return HTTPRequestHandler
