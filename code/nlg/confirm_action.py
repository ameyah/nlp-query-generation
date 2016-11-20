import os
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
os.sys.path.insert(0, parentdir)
from data import constants


def confirm_action(confirm_dict):
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


# confirm_action({'price': 'average', 'distance': 'far', 'cuisine': 'chinese'})