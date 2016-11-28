'''
Created on 16-Nov-2016

@author: shahharshil46
'''


# I want some information on [<CUISINE_TYPE> + (ish/ian/can etc)] restaurants.
# Tell me about the [<Cuisine_TYPE> + (ish/ian/can etc)] restaurants you know about.
# List some [<Cuisine_TYPE> + (ish/ian/can etc)] restaurants.
# Can you find me some [<Cuisine_TYPE> + (ish/ian/can etc)] restaurants.
# What [<Cuisine_TYPE> + (ish/ian/can etc)] restaurants do you know about?
# How about some [<Cuisine_TYPE> + (ish/ian/can etc)] restaurants?
# Do you know about [<Cuisine_TYPE> + (ish/ian/can etc)] restaurants?
# Which restaurants serve [<Cuisine_TYPE> + (ish/ian/can etc)] food?
# I would like to know about restaurants serving [<Cuisine_TYPE> + (ish/ian/can etc)] type of food.
# Find me some [<Cuisine_TYPE> + (ish/ian/can etc)] restaurants.
import os
import nltk
import global_project_settings

def extract_features(post):
    features = {}
    for word in nltk.word_tokenize(post):
        features['contains(%s)' % word.lower()] = True
    return features



def NLU_Classifier_Initiate():
    training_statements = list()
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "restaurants_training_for_nlu.txt")) as f:
        for line in f:
            data = list()
            data.append(line.split("\t")[0].strip())
            data.append(line.split("\t")[1].strip())
    #         print(data)
            training_statements.append(data)
    # print(training_statements)
    
    # print(extract_features("This is a statement"))
    
    # posts = nltk.corpus.nps_chat.xml_posts()[:1]
    # print(posts[0].text)
    
    featuresets = [(extract_features(post[0]), post[1]) for post in training_statements]
    # print(featuresets)
    
    return nltk.DecisionTreeClassifier.train(featuresets)
# print(classifier.pretty_format())
# classifier = nltk.NaiveBayesClassifier.train(featuresets)

def NLU_Classifier_Test(classifier):
#     classifier = global_project_settings.classifier
    test_statements = [
    ["Will you tell me about some korean restaurants.", "korean"] ,
    ["Are there any korean restaurants", "korean"],
    
    ["Will you tell me about some indian restaurants.", "indian"] ,
    ["Are there any indian restaurants", "indian"],
    
    ["Will you tell me about some chinese restaurants.", "chinese"] ,
    ["Are there any chinese restaurants", "chinese"],
    
    ["Will you tell me about some mexican restaurants.", "mexican"] ,
    ["Are there any mexican restaurants", "mexican"],
    
    ["Will you tell me about some italian restaurants.", "italian"] ,
    ["Are there any italian restaurants", "italian"],
    
    ["give me some information on cheap restaurants.", "cheap"],
    ["Any cheap restaurants?", "cheap"],
    
    ["give me some information on average priced restaurants.","average"],
    ["Any average restaurants?","average"],
    
    ["give me some information on expensive restaurants.","expensive"],
    ["Any expensive restaurants?","expensive"],
    
    ["Give me hotel which is near to me.","near"],
    ["find a place to dine which is beside me.","near"],
    
    ["Give me hotel which is average to me.","average"],
    ["find a place to dine which is average distnace beside me.","average"],
    
    ["Give me hotel which is far to me.","far"],
    ["find a place to dine which is far from me.","far"],
    
    ]
    
    test_sets = [(extract_features(post[0]), post[1]) for post in test_statements]
    
    
    
    # print(nltk.classify(classifier, test_sets))
    print(nltk.classify.accuracy(classifier, test_sets))
    
#     st = "cheap restaurants and average"
#     print(classifier.classify((extract_features(st))))
#     
#     st = "Which restaurants have best indian food?"
#     print(classifier.classify((extract_features(st))))
    
#     st = "Give me mediocre restaurants"
#     print(classifier.classify((extract_features(st))))
    
    
def getLabel(classifier, statement):
    label = classifier.classify(extract_features(statement))
    category = ""
    if label in global_project_settings.cuisine_list:
        category = "cuisine"
    elif label in global_project_settings.price_list:
        category = "price"
    elif label in global_project_settings.location_list:
        category = "distance"
    else:
        category = "confirm"

    return [category, label]
