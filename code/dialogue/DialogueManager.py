# not checked for running code, only a draft of Dialogue Manager, NLG implementation has to be done.
import MySQLdb
import os
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
os.sys.path.insert(0, parentdir)
from nlu import keyword_approach
from nlu import NLU_Classification
from nlu import global_project_settings
from nlg import confirm_action
from nlg import request_info as request_info_nlg
from nlg import response_action
from include import utils


class DialogueManager:
    def __init__(self):
        self.userDictionaryConfirmConfirm = {
            'price': None,
            'cuisine': None,
            'distance': None
        }
        self.preferences = {
            'price': None,
            'cuisine': None,
            'distance': None
        }
        self.priorities = []
        self.input_string_from_user = ""
        self.request_info_dict = {
            'price': None,
            'cuisine': None,
            'distance': None
        }
        self.confirm_flag = False
        self.current_confirm_factor = None

    def store_preferences(self, preferences_priorities_dict):
        for preference in preferences_priorities_dict['preferences']:
            self.preferences[preference] = preferences_priorities_dict['preferences'][preference]
        self.priorities = preferences_priorities_dict['priorities']

    def generate_result(self, user_input):
        self.input_string_from_user = user_input
        nlu_info_array = NLU_Classification.getLabel(global_project_settings.classifier, self.input_string_from_user)
        print nlu_info_array
        if self.confirm_flag:
            if nlu_info_array[1] == "yes":
                self.confirm_flag = False
                self.userDictionaryConfirmConfirm[self.current_confirm_factor] = True
                self.current_confirm_factor = None
                all_confirmed = self.is_all_confirmed()
                if all_confirmed:
                    main_results = self.get_results(self.request_info_dict)
                    tradeoff_factor = self.check_tradeoff_factor(self.request_info_dict, self.priorities)
                    tradeoff_results = None
                    if tradeoff_factor:
                        tradeoff_request_dict = {}
                        for key in self.request_info_dict:
                            tradeoff_request_dict[key] = self.request_info_dict[key]
                        tradeoff_request_dict[tradeoff_factor] = self.preferences[tradeoff_factor]
                        tradeoff_results = self.get_results(tradeoff_request_dict)
                    result_str = response_action.response_action(main_results, tradeoff_results)
                    self.confirm_flag = False
                    return {"text": result_str, "main_results": main_results, "tradeoff_results": tradeoff_results}
            elif nlu_info_array[1] == "no":
                self.confirm_flag = False
                self.userDictionaryConfirmConfirm[self.current_confirm_factor] = None
                self.request_info_dict[self.current_confirm_factor] = None
        print self.request_info_dict
        self.request_info_dict = self.compare_dictionaries(self.request_info_dict, nlu_info_array)
        print self.request_info_dict
        self.request_info_dict = self.set_preferences(self.request_info_dict)
        print self.request_info_dict
        while True:
            required_data = self.request_info()
            print required_data
            if required_data:
                request_str = request_info_nlg.request_info(required_data)
                return {"text": request_str}
            else:
                break
        print 'To be confirmed ---'
        print self.request_info_dict
        while True:
            confirm_data = self.confirm_info()
            if confirm_data:
                self.current_confirm_factor = confirm_data
                confirm_str = confirm_action.confirm_action_single(
                    {confirm_data: self.request_info_dict[confirm_data]})
                self.confirm_flag = True
                return {"text": confirm_str}

    def compare_dictionaries(self, main_data, new_data):
        try:
            main_data[new_data[0]] = new_data[1]
            self.userDictionaryConfirmConfirm[new_data[0]] = False
            return main_data
        except KeyError as e:
            return main_data

    def set_preferences(self, request_info_dict):
        for key in request_info_dict:
            if not request_info_dict[key]:
                request_info_dict[key] = self.preferences[key]
        return request_info_dict

    def request_info(self):
        for key in self.request_info_dict:
            if not self.request_info_dict[key]:
                return key

    def confirm_info(self):
        for key in self.userDictionaryConfirmConfirm:
            if not self.userDictionaryConfirmConfirm[key]:
                return key

    def check_tradeoff_factor(self, request_info_dict, priorities):
        for priority in priorities:
            if request_info_dict[priority] != self.preferences[priority]:
                return priority

    """
    def check_for_confirm_value(self, main_dic):
        for key in main_dic:
            if (userDictionaryConfirmConfirm[key] == 'filled' or userDictionaryConfirmConfirm[key] == None )
                return False
        return True
    """

    def is_all_confirmed(self):
        for key in self.userDictionaryConfirmConfirm:
            if not self.userDictionaryConfirmConfirm[key]:
                return False
        return True

    @staticmethod
    def get_results(request_info_dict):
        credentials = utils.dbcredentials(os.path.abspath(__file__))
        connection = MySQLdb.connect(host=credentials["host"],  # your host, usually localhost
                                     user=credentials["user"],  # your username
                                     passwd=credentials["password"],  # your password
                                     db=credentials["db"],
                                     cursorclass=MySQLdb.cursors.SSDictCursor)  # stores result in the server. records as dict
        query = "SELECT name, location, rating, cuisine, price, distance from restaurants where cuisine = {} and \
                distance = {} and price = {}"
        query = query.format(request_info_dict['cuisine'], request_info_dict['distance'], request_info_dict['price'])
        print "Query:" + query
        cursor = connection.cursor()
        cursor.execute(query)
        response = cursor.fetchall()
        cursor.close()
        return response