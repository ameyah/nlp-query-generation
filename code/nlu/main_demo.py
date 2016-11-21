'''
Created on 17-Nov-2016

@author: shahharshil46
'''
import global_project_settings
import NLU_Classification


global_project_settings.init()

# NLU_Classification.NLU_Classifier_Initiate()
NLU_Classification.NLU_Classifier_Test(global_project_settings.classifier)

st = "cheap restaurants and average"
print(NLU_Classification.getLabel(global_project_settings.classifier, st))

st = "no i did not ordered for this"
print(NLU_Classification.getLabel(global_project_settings.classifier, st))