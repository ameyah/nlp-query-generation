import operator
import global_project_settings


training_statements = list()
labeled_data = dict()

def init():
    with open("restaurants_training_for_nlu.txt") as f:
        for line in f:
            labeled_data[line.split("\t")[0].strip()] = line.split("\t")[1].strip()
            training_statements.append(line.split("\t")[0].strip())

def levenshtein(s1, s2):
    if len(s1) < len(s2):
        return levenshtein(s2, s1)

    # len(s1) >= len(s2)
    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[
                             j + 1] + 1  # j+1 instead of j since previous_row and current_row are one character longer
            deletions = current_row[j] + 1  # than s2
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]

def getNeighbors(trainingSet, testInstance, k=1):
    distances = []
    length = len(testInstance)-1
    for x in range(len(trainingSet)):
        dist = levenshtein(testInstance, trainingSet[x])
        distances.append((trainingSet[x], dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors


def getLabel(st):
    label = labeled_data[getNeighbors(training_statements, st, 1)[0]]
    category = ""
    if label in global_project_settings.cuisine_list:
        category = "cuisine"
    elif label in global_project_settings.price_list:
        category = "price"
    elif label in global_project_settings.location_list:
        category = "location"
    else:
        category = "confirm"

    return [category, label]


