from keyword_extract import extract
import os

import gensim

__author__ = 'ameya'

price_keywords = ['cheap', 'average', 'expensive']
cuisine_keywords = ['indian', 'italian', 'korean', 'chinese', 'mexican']
distance_keywords = ['near', 'far', 'average']


def get_structured_input(text_input):
    """
    corenlp_obj = corenlp.StanfordCoreNLP()  # wait a few minutes...
    corenlp_obj.parse(text_input)
    """
    keywords = extract(text_input.lower())
    combined_keywords = [keyword[0] for keyword in keywords]
    combined_keywords = [keyword for keyword in combined_keywords]
    formatted_keywords = []
    for keyword in combined_keywords:
        formatted_keywords.extend(keyword.split())

    formatted_keywords = " ".join(formatted_keywords)

    request_info_dict = {
        'price': None,
        'cuisine': None,
        'distance': None
    }
    # check for price & location
    # check for price
    if "cheap" in formatted_keywords:
        request_info_dict['price'] = "cheap"
    elif "expensive" in formatted_keywords:
        request_info_dict['price'] = "expensive"

    # check for distance
    if "near" in formatted_keywords:
        request_info_dict['distance'] = "near"
        # formatted_keywords[:] = [x for x in formatted_keywords if x != "distance"]
        formatted_keywords = formatted_keywords.replace("distance", "").strip()
    elif "far" in formatted_keywords:
        request_info_dict['distance'] = "far"
        # formatted_keywords[:] = [x for x in formatted_keywords if x != "distance"]
        formatted_keywords = formatted_keywords.replace("distance", "").strip()

    # resolve "average" keyword understanding
    if "average distance" in formatted_keywords:
        if not request_info_dict['distance']:
            request_info_dict['distance'] = "average"
            formatted_keywords = formatted_keywords.replace("average distance", "").strip()

    if "average" in formatted_keywords:
        if not request_info_dict['price']:
            request_info_dict['price'] = "average"
            formatted_keywords = formatted_keywords.replace("average", "").strip()

    # check for cuisine
    for cuisine in cuisine_keywords:
        if cuisine in formatted_keywords:
            request_info_dict['cuisine'] = cuisine
    """
    if "average" in formatted_keywords:
        if not request_info_dict['distance']:
            # average is only related to distance if "distance" keyword is next to "average"

        average_index = formatted_keywords.index("average")
        # check for location
        location_index = None
        if "distance" in formatted_keywords:
            location_index = formatted_keywords.index("distance")
        elif "location" in formatted_keywords:
            location_index = formatted_keywords.index("location")
        if location_index:
            if abs(location_index - average_index) <= 2:
                request_info_dict['distance'] = "average"
                del formatted_keywords[average_index]
                del formatted_keywords[location_index]

        # check for price
        # if "average"
        average_index = formatted_keywords.index("average")
    """


    print request_info_dict

    """
    model_path = "data/GoogleNews-vectors-negative300.bin"
    model = gensim.models.word2vec.Word2Vec.load_word2vec_format(model_path, binary=True)
    model.init_sims(replace=True)
    for keyword in formatted_keywords:
        print model.similar_by_word(keyword)
    """