from keyword_extract import extract
import os
import inspect
import re

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
os.sys.path.insert(0, parentdir)
from data import constants


def replace_synonyms(text_input):
    for key in constants.synonyms:
        for synonym in constants.synonyms[key]:
            if " " + synonym + " " in text_input:
                text_input = text_input.replace(synonym, key)
    return text_input


def set_distance_request(formatted_keywords):
    """
    input_without_distance = formatted_keywords.replace("distance", "").strip()
    explicit_distance_re = re.compile(r'less \d+')
    if explicit_distance_re.search(input_without_distance):
    """

    if "near" in formatted_keywords or "usc" in formatted_keywords:
        return "near"
    elif "far" in formatted_keywords or "marina del rey" in formatted_keywords or "santa monica" in formatted_keywords:
        return "far"
    return None


def rearrange_keywords(input_text, formatted_keywords):
    input_arr = input_text.split()
    rearranged_keywords = []
    for word in input_arr:
        if word in formatted_keywords:
            rearranged_keywords.append(word)
    return rearranged_keywords


def get_structured_input(text_input):
    text_input = replace_synonyms(text_input.lower().replace('-', " "))
    # Sometimes, keyword extraction returns empty list. Beware!
    keywords = extract(text_input.lower())
    # print keywords
    combined_keywords = [keyword[0] for keyword in keywords]
    combined_keywords = [keyword for keyword in combined_keywords]
    formatted_keywords = []
    for keyword in combined_keywords:
        formatted_keywords.extend(keyword.split())

    formatted_keywords = rearrange_keywords(text_input.lower(), formatted_keywords)
    print formatted_keywords

    formatted_keywords = " ".join(formatted_keywords)
    # print formatted_keywords
    # replace synonyms called twice because: after keyword extraction, ONLY keywords might invoke replacement of some
    # synonyms
    # For eg. I want a restaurant not so far away
    formatted_keywords = replace_synonyms(formatted_keywords)

    print formatted_keywords

    # TODO: consider stemming words in dictionary and from input sentence

    request_info_dict = {
        'price': None,
        'cuisine': None,
        'distance': None,
        'confirm': None
    }
    # check for price & location
    # check for price
    if "cheap" in formatted_keywords:
        request_info_dict['price'] = "cheap"
    elif "expensive" in formatted_keywords:
        request_info_dict['price'] = "expensive"

    # check for distance
    request_info_dict['distance'] = set_distance_request(formatted_keywords)
    if request_info_dict['distance']:
        formatted_keywords = formatted_keywords.replace("distance", "").strip()

    # resolve "average" keyword understanding
    if "average distance" in formatted_keywords or "distance average" in formatted_keywords:
        if not request_info_dict['distance']:
            request_info_dict['distance'] = "average"
            formatted_keywords = formatted_keywords.replace("average distance", "").strip().replace("distance average",
                                                                                                    "").strip()

    if "average" in formatted_keywords:
        if not request_info_dict['price']:
            request_info_dict['price'] = "average"
            formatted_keywords = formatted_keywords.replace("average", "").strip()

    # check for cuisine
    for cuisine in constants.cuisine_keywords:
        if cuisine in formatted_keywords:
            request_info_dict['cuisine'] = cuisine

    return request_info_dict