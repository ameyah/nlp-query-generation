from BaseHTTPServer import BaseHTTPRequestHandler
import json
from include import utils
from dialogue import DialogueManager_KeyWord, DialogueManager


def HTTPRequestHandlerContainer():

    dialogue_manager = None

    class HTTPRequestHandler(BaseHTTPRequestHandler):

        def __init__(self, request, client_address, server):
            BaseHTTPRequestHandler.__init__(self, request, client_address, server)

        # handle POST command
        def do_POST(self):
            print self.path
            if "/preferences" in self.path:
                global dialogue_manager
                dialogue_manager = DialogueManager_KeyWord.DialogueManager()
                postvars = utils.get_post_data(self.headers, self.rfile)
                if postvars != '':
                    preferences = None
                    try:
                        for key in postvars:
                            preferences = json.loads(key)
                    except TypeError as e:
                        self.send_bad_request_response()
                    if preferences:
                        dialogue_manager.store_preferences(preferences)

                    self.send_ok_response()
                else:
                    self.send_bad_request_response()
            elif "/getresults" in self.path:
                postvars = utils.get_post_data(self.headers, self.rfile)
                user_input = ''
                if postvars != '':
                    try:
                        for key in postvars:
                            user_input = key
                            break
                    except TypeError as e:
                        self.send_bad_request_response()
                        return
                    if user_input != '':
                        result = dialogue_manager.generate_result(user_input)
                        self.send_ok_response(data=json.dumps(result))

        # handle GET command
        def do_GET(self):
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
