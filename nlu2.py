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
import speech_recognition as sr
from gtts import gTTS

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
["low-priced cheap competitive economical low-cost low-priced reasonable bargain bargain-basement bargain-counter budget cheapo cost cut-price cut-rate depreciated half-priced lowered reduced slashed standard uncostly affordable bargain-basement cheapie cheapo chintzy cut-price cut-rate dime-store dirt cheap el cheapo low price low-end popular reasonable cheapish moderate discount discounted fire-sale lowered reduced wholesale supercheap ultracheap stingy chintzy closefisted penny-pinching easy-priced soft-priced", "cheap"],

["I want some average restaurants.","average"],
["Which restaurants are average ?","average"],
["Only give me all average hotels?","average"],
["Food places that are average priced?","average"],
["Can i have restaurants that are average?","average"],
["Find me some average restaurants?","average"],
["Need a place which provides average food pricing ?","average"],
["average nice restaurants", "average"],
["Search me some average restaurants.","average"],
["acceptable equitable fair feasible honest humane impartial judicious justifiable legitimate modest plausible proper prudent rational restrained sane sensible understandable valid analytical average circumspect conservative controlled discreet Legit making sense okay right sound within reasonable limit curbed disciplined inhibited restrained calculated deliberate measured levelheaded rational reasonable sensible mediocre medium modest so-so; normal ordinary regular routine typical usual", "average"],

# ["Tell me about some average restaurants.","average"],
# ["Are there any average restaurants", "average"],
["I want some expensive restaurants.","expensive"],
["Which restaurants are expensive ?","expensive"],
["Only give me all expensive hotels?","expensive"],
["Food places that are expensive priced?","expensive"],
["Can i have restaurants that are expensive?","expensive"],
["Find me some expensive restaurants?","expensive"],
["Need a place which provides expensive food pricing ?","expensive"],
["Tell me about some expensive restaurants.","expensive"],
["Search me some expensive restaurants.","expensive"],
["costly extravagant fancy high lavish overpriced pricey upscale valuable premium big-ticket excessive exorbitant holdup immoderate inordinate plush posh rich ritzy sky-high steep stiff swank", "expensive"],

# Restaurants based on location

["I want to know about restaurants located near short close nearby closeby convenient neighboring me.","near"],
["Tell me about restaurants located approximately less then zero to ten MILES close short nearby closeby convenient neighboring away from here.","near"],
["Find me some restaurants located near or moderately near short close nearby closeby convenient neighboring from here.","near"],
["Okay tell me about restaurants near close nearby closeby short convenient neighboring distance from here.","near"],
["Give me neighboring near close nearby closeby convenient short food places?","near"],
["What are next close nearby closeby convenient near short neighboring door restaurants for me?","near"],
["Give me in close nearby closeby convenient near short neighboring proximity restaurants?","near"],
["Give near close nearby closeby convenient neighboring short list of restaurants?","near"],
#["I want to know about restaurants located within reach short to me.","near"],
#["Tell me about restaurants located approximately short within reach from here.","near"],
#["Find me some restaurants located within reach or moderately near short from here.","near"],
#["Okay tell me about restaurants within reach short distance from here.","near"],
#["Give me within reach food places?","near"],
#["What are within reach restaurants for me?","near"],
#["Give me in within reach restaurants?","near"],
#["I want to know about restaurants located around the corner to me.","near"],
#["Tell me about restaurants located approximately around the corner away from here.","near"],
#["Find me some restaurants located around the corner from here.","near"],
#["Okay tell me about restaurants around the corner distance from here.","near"],
#["Give me around the corner food places?","near"],
#["What are around the corner restaurants for me?","near"],
#["Give me around the corner proximity restaurants?","near"],
#["Give around the corner list of restaurants?","near"],

["I want to know about restaurants located average fair intermediate medial mediocre midway centre me.","fair"],
["Tell me about restaurants located approximately less then eleven to twenty MILES fair intermediate medial mediocre midway centre away from here.","fair"],
["Find me some restaurants located average or moderately average fair intermediate medial mediocre midway centre from here.","fair"],
["Okay tell me about restaurants average fair intermediate medial mediocre midway centre distance from here.","fair"],
["Give me fair intermediate medial mediocre midway centre food places?","fair"],
["What are further from next door fair intermediate medial mediocre midway centre restaurants for me?","fair"],
["Give me in average fair intermediate medial mediocre midway centre proximity restaurants?","fair"],
["Give fair intermediate medial mediocre midway centre list of restaurants?","fair"],

["I want to know about restaurants located far distant remote far-flung outlaying outlier long way miles afar off me.","far"],
["Tell me about restaurants located approximately more then twetyonne to thirty MILES distant remote far-flung outlaying outlier long way miles afar off away from here.","far"],
["Find me some restaurants located far distant remote far-flung outlaying outlier long way miles afar off or moderately far from here.","far"],
["Okay tell me about restaurants away distant remote far-flung outlaying outlier long way miles afar off from here.","far"],
["Give me far distant remote far-flung outlaying outlier long way miles afar off food places?","far"],
["What are extreme door distant remote far-flung outlaying outlier long way miles afar off restaurants for me?","far"],
["Give me in far distant remote far-flung outlaying outlier long way miles afar off proximity restaurants?","far"],
["Give far distant remote far-flung outlaying outlier long way miles afar off list of restaurants?","far"],

]



def extract_features(post):
    features = {}
    for word in nltk.word_tokenize(post):
        features['contains(%s)' % word.lower()] = True
    return features

#print(extract_features("This is a statement"))

# posts = nltk.corpus.nps_chat.xml_posts()[:1]
# print(posts[0].text)

featuresets = [(extract_features(post[0]), post[1]) for post in training_statements]
#print(featuresets)

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

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)
 
# Speech recognition using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    #print("You said: " + r.recognize_google(audio))
	print ("Speech part classification running")
	print (r.recognize_google(audio))
	print (classifier.classify(extract_features(r.recognize_google(audio))))
	#tts = gTTS(text=r.recognize_google(audio), lang='en')
	#print 
	#tts.save('hello.mp3')
	#os.system('hello.mp3')
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

# print(nltk.classify(classifier, test_sets))
#print(nltk.classify.accuracy(classifier, test_sets))

st = "cheap restaurants and average"
#print(classifier.classify((extract_features(st))))

st = "Which restaurants have best indian food?"
#print(classifier.classify((extract_features(st))))

st = "Give me restaurant which is in a far proximity"
#print(classifier.classify((extract_features(st))))