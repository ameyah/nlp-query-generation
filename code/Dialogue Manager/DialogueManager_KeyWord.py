#not checked for running code, only a draft of Dialogue Manager, NLG implementation has to be done.
import pyodbc
import nltk
import NLU_Classification
import global_project_settings

 
userDictionaryConfirmConfirm=dict()
userDictionaryConfirm["cuisine"]=["empty"]
userDictionaryConfirm["price"]=["empty"]
userDictionaryConfirm["distance"]=["empty"]
#userDictionaryConfirm["star"]=["empty"]

request_info_dict = {
        'price': None,
        'cuisine': None,
        'distance': None
    }



def request_info(request_info_dict):
    if not request_info_dict['price']:
        return constants.request_price
    if not request_info_dict['cuisine']:
        return constants.request_cuisine
    if not request_info_dict['distance']:
        return constants.request_distance

def confirm_action(request_info_dict):
    if not request_info_dict['price']:
		userDictionaryConfirm["price"]=request_info_dict['price']
    if not request_info_dict['cuisine']:
		userDictionaryConfirm["cuisine"]=request_info_dict['cuisine']
    if not request_info_dict['distance']:
		userDictionaryConfirm["distance"]=request_info_dict['distance']
	return userDictionaryConfirm
		

		
		
# we have all required input at this point, can now query the DB.


cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost;DATABASE=testdb;UID=me;PWD=pass')
cursor = cnxn.cursor()
cursor.execute("select cuisine from db where cuisine=val")
rows = cursor.fetchall()
for row in rows:
    print row.hotel_name, row.hotel_place
