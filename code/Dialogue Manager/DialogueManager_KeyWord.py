#not checked for running code, only a draft of Dialogue Manager, NLG implementation has to be done.
import pyodbc
import nltk
import NLU_Classification
import global_project_settings
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
os.sys.path.insert(0, parentdir)
from data import constants
from nlu import keyword_approach
from nlg import confirm_action
from nlg import request_info
from nlg import response_action
 
userDictionaryConfirmConfirm=dict()
userDictionaryConfirm["cuisine"]=["empty"]
userDictionaryConfirm["price"]=["empty"]
userDictionaryConfirm["distance"]=["empty"]

#request_info_dict = {
#        'price': None,
#        'cuisine': None,
#        'distance': None
#    }

input_string_from_user=""

request_info_dict=dict()
request_info_dict = get_structured_input("give me indian restaurant near me which are cheap")
#request_info_dict = get_structured_input(input_string_from_user)


def request_info(request_info_dict):
    if not request_info_dict['price']:
        request_info_nlu(constants.request_price)
    if not request_info_dict['cuisine']:
        request_info_nlu(constants.request_cuisine)
    if not request_info_dict['distance']:
        request_info_nlu(constants.request_distance)

def confirm_action(request_info_dict):
    if not request_info_dict['price']:
		userDictionaryConfirm["price"]=request_info_dict['price']
    if not request_info_dict['cuisine']:
		userDictionaryConfirm["cuisine"]=request_info_dict['cuisine']
    if not request_info_dict['distance']:
		userDictionaryConfirm["distance"]=request_info_dict['distance']
	confirm_action(userDictionaryConfirm)
		

		
		
# we have all required input at this point, can now query the DB.
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost;DATABASE=testdb;UID=me;PWD=pass')
cursor = cnxn.cursor()
cursor.execute("select cuisine from db where cuisine=val")
rows = cursor.fetchall()
for row in rows:
    print row.hotel_name, row.hotel_place
