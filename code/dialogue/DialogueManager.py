#not checked for running code, only a draft of Dialogue Manager, NLG implementation has to be done.
import pyodbc
import nltk
import NLU_Classification
import global_project_settings

 
userDictionary=dict()
userDictionary["cuisine"]=["empty","empty"]
userDictionary["price"]=["empty","empty"]
userDictionary["distance"]=["empty","empty"]
#userDictionary["star"]=["empty","empty"]

#cuisine=["empty","chinese","indian","italian","korean","mexican"]
#price=["empty","cheap","average","expensive"]
#location=["empty","near","fair","far"]
#star=["empty","best","moderate","worst"]

#listResult=NLU_Classification.getLabel(global_project_settings.classifier,st)
#provided_label_for_classification=list[0]
#provde_info=listResult[1]

provided_label_for_classification="cuisine" # Label classification class also need to be provided from NLU logic
provide_info="indian" #taken dummy input as in user has asked for Indian cuisine

#Update user Dictionary

#loop runs until all values of user dictionary are filled with confirm type or no value is equal to empty.
#loop also needs to interact with NLU and NLG frequently
count = 0
keyreuired=""
while(count <= 2 ):
	for key in userDictionary:
		if(userDictionary[key][0]=="empty"):
			keyreuired=key
			break
	request_info=request_info(keyreuired)
	##NLGFunction_request implementation remaining
	provided_label_for_classification=request_info[0]
	provide_info=request_info[1]
	userDictionary[provided_label_for_classification][0]=provide_info
	userDictionary[provided_label_for_classification][1]="filled"
	#send user a confirmation dialogue act if status for label is filled
	
	if (userDictionary[provided_label_for_classification][1]=="filled"):
		#send this to NLG
		confirm_dialogueAct=[provided_label_for_classification,provide_info]
		confirm_Received=confirm_action(confirm_dialogueAct)
		##NLGFunction_confirm implementation remaining
		if(confirm_Received=="yes"):
			userDictionary[provided_label_for_classification][1]="confirm"
			count=count+1
		else
			userDictionary[provided_label_for_classification][1]="empty"
		
			
		
		
# we have all required input at this point, can now query the DB.


cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost;DATABASE=testdb;UID=me;PWD=pass')
cursor = cnxn.cursor()
cursor.execute("select cuisine from db where cuisine=val")
rows = cursor.fetchall()
for row in rows:
    print row.hotel_name, row.hotel_place
