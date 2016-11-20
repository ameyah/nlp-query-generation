import os
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
os.sys.path.insert(0, parentdir)
from data import constants


def request_info(attribute):
    if attribute == "price":
        return constants.request_price
    if attribute == "cuisine":
        return constants.request_cuisine
    if attribute == "distance":
        return constants.request_distance