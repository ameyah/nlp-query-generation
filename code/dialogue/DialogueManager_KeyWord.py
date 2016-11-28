# not checked for running code, only a draft of Dialogue Manager, NLG implementation has to be done.
import MySQLdb
import os
import inspect
import json

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
os.sys.path.insert(0, parentdir)
from nlu import keyword_approach
from nlg import confirm_action
from nlg import request_info as request_info_nlg
from nlg import response_action
from include import utils
from include import db_conn


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
        self.db_connection = db_conn.DbConnection()

    def store_preferences(self, preferences_priorities_dict):
        for preference in preferences_priorities_dict['preferences']:
            self.preferences[preference] = preferences_priorities_dict['preferences'][preference]
        self.priorities = preferences_priorities_dict['priorities']

    def generate_result(self, user_input):
        self.input_string_from_user = user_input
        nlu_info_dict = keyword_approach.get_structured_input(self.input_string_from_user)
        if self.confirm_flag:
            if nlu_info_dict['confirm'] == True:
                main_results = self.get_results(self.request_info_dict)
                tradeoff_factor = self.check_tradeoff_factor(self.request_info_dict, self.priorities)
                tradeoff_results = None
                if tradeoff_factor:
                    tradeoff_request_dict = {}
                    for key in self.request_info_dict:
                        tradeoff_request_dict[key] = self.request_info_dict[key]
                    tradeoff_request_dict[tradeoff_factor] = self.preferences[tradeoff_factor]
                    tradeoff_results = self.get_results(tradeoff_request_dict)
                result_str = response_action.response_action(main_results, tradeoff_factor, tradeoff_results)
                self.confirm_flag = False
                return {"text": result_str, "main_results": main_results, "tradeoff_results": tradeoff_results}
            else:
                self.confirm_flag = False
                for key in self.request_info_dict:
                    self.request_info_dict[key] = None
                for key in nlu_info_dict:
                    nlu_info_dict[key] = None

        self.request_info_dict = self.compare_dictionaries(self.request_info_dict, nlu_info_dict)
        self.request_info_dict = self.set_preferences(self.request_info_dict)
        while True:
            required_data = self.request_info()
            if required_data:
                request_str = request_info_nlg.request_info(required_data)
                return {"text": request_str}
            else:
                break
        print 'To be confirmed ---'
        print self.request_info_dict
        confirm_str = confirm_action.confirm_action_all(self.request_info_dict)
        self.confirm_flag = True
        return {"text": confirm_str}

    @staticmethod
    def compare_dictionaries(main_data, new_data):
        for key in new_data:
            if new_data[key]:
                main_data[key] = new_data[key]
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

    def check_tradeoff_factor(self, request_info_dict, priorities):
        for priority in priorities:
            if request_info_dict[priority] != self.preferences[priority]:
                if self.preferences[priority] :
                    return priority

    def get_results(self, request_info_dict):
        print request_info_dict
        query = "SELECT name, location, rating, cuisine, price, distance from restaurants where cuisine = '{}' and \
                distance = '{}' and price = '{}' ORDER BY rating DESC"
        query = query.format(request_info_dict['cuisine'].title(), request_info_dict['distance'].upper(), request_info_dict['price'].upper())
        cursor = self.db_connection.get_cursor()
        print "Query:" + query
        cursor.execute(query)
        response = cursor.fetchall()
        print response
        cursor.close()
        return response