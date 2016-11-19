import os
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
os.sys.path.insert(0, parentdir)
from data import constants


def confirm_action(confirm_dict):
    # sanitize price
    if confirm_dict['price'] == "cheap":
        confirm_dict['price'] = "a cheap"
    elif confirm_dict['price'] == "average":
        confirm_dict['price'] = "an average priced"
    elif confirm_dict['price'] == "expensive":
        confirm_dict['price'] = "an expensive"

    if confirm_dict['distance'] == "average":
        confirm_dict['distance'] = "at an average distance"
    return constants.confirm.format(confirm_dict['price'], confirm_dict['cuisine'], confirm_dict['distance'])


# confirm_action({'price': 'average', 'distance': 'far', 'cuisine': 'chinese'})