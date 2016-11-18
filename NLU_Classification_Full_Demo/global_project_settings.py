'''
Created on 17-Nov-2016

@author: shahharshil46
'''


import nltk
import NLU_Classification

def init():
    global classifier
    global cuisine_list
    global price_list
    global location_list
    global star_list
    classifier = NLU_Classification.NLU_Classifier_Initiate()
    print("Classifier training completed")
    
    
classifier = ""

cuisine_list=["chinese","indian","italian","korean","mexican"]
price_list=["cheap","average","expensive"]
location_list=["near","fair","far"]
star_list=["best","moderate","worst"]