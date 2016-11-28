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
print(KNN_methods.getLabel(s1))