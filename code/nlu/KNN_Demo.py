import KNN_methods


KNN_methods.init()
s1 = "Tell me about the indian restaurants you know about."
s1 = "I want a restaurant which is near"
s1 = "I am looking for an average priced restaurant"
# s1 = "no"
# s1 = "no"
# neighbors = getNeighbors(training_statements, s1, 1)
# print(neighbors)
# print(labeled_data[neighbors[0]])
# print(KNN_methods.getLabel(s1))

test_statements = [
    ["Will you tell me about some korean restaurants.", "korean"],
    ["Are there any korean restaurants", "korean"],

    ["Will you tell me about some indian restaurants.", "indian"],
    ["Are there any indian restaurants", "indian"],

    ["Will you tell me about some chinese restaurants.", "chinese"],
    ["Are there any chinese restaurants", "chinese"],

    ["Will you tell me about some mexican restaurants.", "mexican"],
    ["Are there any mexican restaurants", "mexican"],

    ["Will you tell me about some italian restaurants.", "italian"],
    ["Are there any italian restaurants", "italian"],

    ["give me some information on cheap restaurants.", "cheap"],
    ["Any cheap restaurants?", "cheap"],

    ["give me some information on average priced restaurants.", "average"],
    ["Any average restaurants?", "average"],

    ["give me some information on expensive restaurants.", "expensive"],
    ["Any expensive restaurants?", "expensive"],

    ["Give me hotel which is near to me.", "near"],
    ["find a place to dine which is beside me.", "near"],

    ["Give me hotel which is average to me.", "average"],
    ["find a place to dine which is average distnace beside me.", "average"],

    ["Give me hotel which is far to me.", "far"],
    ["find a place to dine which is far from me.", "far"],

    ["Oh yea", "yes"],
    ["yeah, that is correct", "yes"],

    ["Naah, not that one", "no"],
    ["nope", "no"],

    ["give me some information about restaurants at an average distance .", "fair"],
    ["Any average distanced restaurants?", "fair"]

]

test_sets = [(post[0], post[1]) for post in test_statements]
count = 0
for sentence, label in test_sets:
    opLabel = KNN_methods.getLabel(sentence)
    print(sentence + " is classified as " + opLabel[1])
    if(opLabel[1] == label):
        count+=1

print(str(count) + "/"+ str(len(test_sets)) + " correct. " + str(count * 100 /(len(test_sets))) + "% accuracy.")
