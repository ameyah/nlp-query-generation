from BaseHTTPServer import BaseHTTPRequestHandler
import json
from controllers import Controllers
import include.util as utils
import MySQLdb

__author__ = 'Ameya'


def HTTPRequestHandlerContainer():

    controller = Controllers()

    class HTTPRequestHandler(BaseHTTPRequestHandler):

        def __init__(self, request, client_address, server):
            BaseHTTPRequestHandler.__init__(self, request, client_address, server)
            # self.controller = Controllers()

        # handle POST command
        def do_POST(self):
            print self.path
            if "/prestudy/answers" in self.path:
                postvars = utils.get_post_data(self.headers, self.rfile)
                if postvars != '':
                    result = controller.insert_prestudy_answers(postvars)
                    self.send_ok_response(data=result)
                else:
                    self.send_bad_request_response()

            elif "/poststudy/answers" in self.path:
                postvars = utils.get_post_data(self.headers, self.rfile)
                if postvars != '':
                    result = controller.insert_poststudy_answers(postvars)
                    self.send_ok_response(data=result)
                else:
                    self.send_bad_request_response()

            elif "/website/save" in self.path:
                postvars = utils.get_post_data(self.headers, self.rfile)
                if postvars != '':
                    controller.save_user_website_list(postvars)
                    self.send_ok_response()
                else:
                    self.send_bad_request_response()

            elif "/participant/id" in self.path:
                postvars = utils.get_post_data(self.headers, self.rfile)
                # set current active participant
                if postvars != '':
                    controller.set_participant_id(postvars)
                    self.send_ok_response()
                else:
                    self.send_bad_request_response()

            elif "/participant/website/add" in self.path:
                postvars = utils.get_post_data(self.headers, self.rfile)
                if postvars != '':
                    result = controller.add_new_user_website(postvars)
                    self.send_ok_response(data=result)
                else:
                    self.send_bad_request_response()

            elif "/participant/website" in self.path:
                postvars = utils.get_post_data(self.headers, self.rfile)
                # set current active participant
                if postvars != '':
                    controller.set_active_website(postvars)
                    self.send_ok_response()
                else:
                    self.send_bad_request_response()

            else:
                self.send_bad_request_response()

        # handle GET command
        def do_GET(self):
            try:
                if "/online" in self.path:
                    self.send_ok_response(data=1)

                elif "/participant/id" in self.path:
                    one_way_hash = utils.get_get_param(self.path, 'hash')
                    participant_id = controller.new_participant_record(one_way_hash)
                    self.send_ok_response(data=participant_id)

                elif "/study/questions" in self.path:
                    question_type = utils.get_get_param(self.path, 'type')
                    result = controller.get_study_questions(question_type)
                    self.send_ok_response(data=json.dumps(result))

                elif "/transform" in self.path:
                    clear_password = utils.get_get_param(self.path, 'pass')
                    try:
                        clear_username = utils.get_get_param(self.path, 'user')
                    except KeyError:
                        clear_username = None
                    try:
                        password_strength = utils.get_get_param(self.path, 'strength')
                    except KeyError:
                        password_strength = 0
                    try:
                        password_warning = utils.get_get_param(self.path, 'warning')
                    except KeyError:
                        password_warning = ""
                    active_url = utils.get_get_param(self.path, 'url')
                    website_info_dict = {
                        'clear_password': clear_password,
                        'clear_username': clear_username,
                        'password_strength': password_strength,
                        'password_warning': password_warning,
                        'active_url': active_url
                    }
                    self.send_ok_response()
                    controller.transform_credentials(website_info_dict)
                elif "/participant/results" in self.path:
                    one_way_hash = utils.get_get_param(self.path, 'hash')
                    result_dict = controller.get_participant_results(one_way_hash)
                    self.send_ok_response(data=json.dumps(result_dict))
                elif "/website/importance" in self.path:
                    website_url = utils.get_get_param(self.path, 'url')
                    importance = controller.get_website_importance(website_url)
                    if importance is not None:
                        self.send_ok_response(data=importance)
                    else:
                        self.send_bad_request_response()
                elif "/website/list/importance" in self.path:
                    website_urls = utils.get_get_param(self.path, 'urls')
                    website_importance_data = controller.get_website_list_probability(website_urls)
                    self.send_ok_response(data=json.dumps(website_importance_data))
                elif "/auth" in self.path:
                    auth_status = utils.get_get_param(self.path, 'success')
                    controller.save_auth_status(auth_status)
                    self.send_ok_response()
                else:
                    self.send_bad_request_response()
            except MySQLdb.Error as e:
                print e
                print "exception"
                clear_password = ''
                controller.clear_plain_text_data()

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
