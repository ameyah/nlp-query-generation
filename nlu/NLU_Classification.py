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
import nltk

training_statements = [
    
# Restaurants based training set
["I want some information on korean restaurants.", "korean"] ,
["Tell me about the korean restaurants you know about.", "korean"],
["List some korean restaurants.", "korean"],
["Can you find me some korean restaurants.", "korean"],
["What korean restaurants do you know about?", "korean"],
["How about some korean restaurants?", "korean"],
["Do you know about korean restaurants?", "korean"],
["Which restaurants serve korean food?", "korean"],
["I would like to know about restaurants serving korean type of food.", "korean"],
["Find me some korean restaurants.", "korean"],

["I want some information on indian restaurants.", "indian"] ,
["Tell me about the indian restaurants you know about.", "indian"],
["List some indian restaurants.", "indian"],
["Can you find me some indian restaurants.", "indian"],
["What indian restaurants do you know about?", "indian"],
["How about some indian restaurants?", "indian"],
["Do you know about indian restaurants?", "indian"],
["Which restaurants serve indian food?", "indian"],
["I would like to know about restaurants serving indian type of food.", "indian"],
["Find me some indian restaurants.", "indian"],

["I want some information on italian restaurants.", "italian"] ,
["Tell me about the italian restaurants you know about.", "italian"],
["List some italian restaurants.", "italian"],
["Can you find me some italian restaurants.", "italian"],
["What italian restaurants do you know about?", "italian"],
["How about some italian restaurants?", "italian"],
["Do you know about italian restaurants?", "italian"],
["Which restaurants serve italian food?", "italian"],
["I would like to know about restaurants serving italian type of food.", "italian"],
["Find me some italian restaurants.", "italian"],

["I want some information on chinese restaurants.", "chinese"] ,
["Tell me about the chinese restaurants you know about.", "chinese"],
["List some chinese restaurants.", "chinese"],
["Can you find me some chinese restaurants.", "chinese"],
["What chinese restaurants do you know about?", "chinese"],
["How about some chinese restaurants?", "chinese"],
["Do you know about chinese restaurants?", "chinese"],
["Which restaurants serve chinese food?", "chinese"],
["I would like to know about restaurants serving chinese type of food.", "chinese"],
["Find me some chinese restaurants.", "chinese"],

["I want some information on mexican restaurants.", "mexican"] ,
["Tell me about the mexican restaurants you know about.", "mexican"],
["List some mexican restaurants.", "mexican"],
["Can you find me some mexican restaurants.", "mexican"],
["What mexican restaurants do you know about?", "mexican"],
["How about some mexican restaurants?", "mexican"],
["Do you know about mexican restaurants?", "mexican"],
["Which restaurants serve mexican food?", "mexican"],
["I would like to know about restaurants serving mexican type of food.", "mexican"],
["Find me some mexican restaurants.", "mexican"],

# Restaurants based on cuisine set

# restaurants based on price

["I want some cheap restaurants.", "cheap"],
["Which restaurants are cheap ?", "cheap"],
["Only give me all cheap hotels?", "cheap"],
["Food places that are cheap priced?", "cheap"],
["Can i have restaurants that are cheap?", "cheap"],
["Find me some cheap restaurants?", "cheap"],
["Need a place which provides cheap food pricing ?", "cheap"],
["Tell me about some cheap restaurants.", "cheap"],
["Search me some cheap restaurants.", "cheap"],

["I want some average restaurants.","average"],
["Which restaurants are average ?","average"],
["Only give me all average hotels?","average"],
["Food places that are average priced?","average"],
["Can i have restaurants that are average?","average"],
["Find me some average restaurants?","average"],
["Need a place which provides average food pricing ?","average"],
# ["Tell me about some average restaurants.","average"],
# ["Are there any average restaurants", "average"],
["average nice restaurants", "average"],
["Search me some average restaurants.","average"],
["I want some expensive restaurants.","expensive"],
["Which restaurants are expensive ?","expensive"],
["Only give me all expensive hotels?","expensive"],
["Food places that are expensive priced?","expensive"],
["Can i have restaurants that are expensive?","expensive"],
["Find me some expensive restaurants?","expensive"],
["Need a place which provides expensive food pricing ?","expensive"],
["Tell me about some expensive restaurants.","expensive"],
["Search me some expensive restaurants.","expensive"],

# Restaurants based on location

["I want to know about restaurants located near me.","near"],
["Tell me about restaurants located approximately less then 10 MILES away from here.","near"],
["Find me some restaurants located near or moderately near from here.","near"],
["Okay tell me about restaurants near distance from here.","near"],
["Give me neighboring food places?","near"],
["What are next door restaurants for me?","near"],
["Give me in close proximity restaurants?","near"],
["Give near list of restaurants?","near"],

["I want to know about restaurants located average me.","average"],
["Tell me about restaurants located approximately less then 20 MILES away from here.","average"],
["Find me some restaurants located average or moderately average from here.","average"],
["Okay tell me about restaurants average distance from here.","average"],
["Give me neighbouring food places?","average"],
["What are further from next door restaurants for me?","average"],
["Give me in average proximity restaurants?","average"],
["Give near list of restaurants?","average"],

["I want to know about restaurants located far me.","far"],
["Tell me about restaurants located approximately more then 30 MILES away from here.","far"],
["Find me some restaurants located far or moderately far from here.","far"],
["Okay tell me about restaurants away from here.","far"],
["Give me afar food places?","far"],
["What are extreme door restaurants for me?","far"],
["Give me in far proximity restaurants?","far"],
["Give far list of restaurants?","far"],

]



def extract_features(post):
    features = {}
    for word in nltk.word_tokenize(post):
        features['contains(%s)' % word.lower()] = True
    return features

print(extract_features("This is a statement"))

# posts = nltk.corpus.nps_chat.xml_posts()[:1]
# print(posts[0].text)

featuresets = [(extract_features(post[0]), post[1]) for post in training_statements]
print(featuresets)

classifier = nltk.NaiveBayesClassifier.train(featuresets)

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

st = "cheap restaurants and average"
print(classifier.classify((extract_features(st))))

st = "Which restaurants have best indian food?"
print(classifier.classify((extract_features(st))))

st = "Give me restaurant which is in a far proximity"
print(classifier.classify((extract_features(st))))
