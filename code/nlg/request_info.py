import os
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
os.sys.path.insert(0, parentdir)
from data import constants


def request_info(request_info_dict):
    if not request_info_dict['price']:
        return constants.request_price
    if not request_info_dict['cuisine']:
        return constants.request_cuisine
    if not request_info_dict['distance']:
        return constants.request_distance