import os
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
os.sys.path.insert(0, parentdir)
from data import constants


def confirm_action_all(confirm_dict):
    # sanitize price
    if confirm_dict['price'] == "cheap":
        price = "a cheap"
    elif confirm_dict['price'] == "average":
        price = "an average priced"
    elif confirm_dict['price'] == "expensive":
        price = "an expensive"
    distance = confirm_dict["distance"]
    if confirm_dict['distance'] == "average":
        distance = "at an average distance"
    return constants.confirm.format(price, confirm_dict['cuisine'], distance)


def confirm_action_single(confirm_dict):
    if 'price' in confirm_dict:
        if confirm_dict['price'] == "cheap":
            price = "less costlier"
        elif confirm_dict['price'] == "average":
            price = "medium priced"
        elif confirm_dict['price'] == "expensive":
            price = "expensive"
        return constants.confirm_price.format(price)
    elif 'distance' in confirm_dict:
        distance = confirm_dict['distance']
        if confirm_dict['distance'] == "average":
            distance = "at an average distance"
        return constants.confirm_distance.format(distance)
    elif 'cuisine' in confirm_dict:
        return constants.confirm_cuisine.format(confirm_dict['cuisine'])
    # confirm_action({'price': 'average', 'distance': 'far', 'cuisine': 'chinese'})