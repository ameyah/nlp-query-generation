# expected data format: [{'name': 'Anocha', 'location': 'USC', 'cuisine': 'Mexican', 'price'; 'cheap'},
# {.....}, {.....}, {....}]
# Use MySQLdb library
import os
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
os.sys.path.insert(0, parentdir)
from data import constants


def get_best_restaurants(result_data):
    """
    This function considers restaurant service rating to determine the best restaurant
    :param result_data: List of dictionaries containing matched restaurant data
    :return: list of best 2 restaurant information in dict
    """
    best_restaurants = []
    for restaurant in result_data:
        if len(best_restaurants) < 2:
            best_restaurants.append(restaurant)
        else:
            if best_restaurants[0]['rating'] > best_restaurants[1]['rating']:
                temp_restaurant = best_restaurants[1]
                best_restaurants[1] = best_restaurants[0]
                best_restaurants[0] = temp_restaurant
            if best_restaurants[0]['rating'] < restaurant['rating']:
                best_restaurants[0] = restaurant
            elif best_restaurants[1]['rating'] < restaurant['rating']:
                best_restaurants[1] = restaurant
    return best_restaurants


def response_action(result_data, tradeoff_factor, tradeoff_data):
    total_restaurants = len(result_data)
    if total_restaurants == 0:
        response = constants.response_no_restaurants
    else:
        if total_restaurants == 1:
            restaurant_count_str = "1 restaurant"
        else:
            restaurant_count_str = str(total_restaurants) + " restaurants"
        # best_restaurants = get_best_restaurants(result_data)
        if len(result_data) == 1:
            response = constants.response_restaurant_count.format(
                restaurant_count_str) + constants.response_restaurant_name_single.format(result_data[0]['name'],
                                                                                         result_data[0]['location'])
        else:
            response = constants.response_restaurant_count.format(
                restaurant_count_str) + constants.response_restaurant_names.format(result_data[0]['name'],
                                                                                   result_data[0]['location'],
                                                                                   result_data[1]['name'],
                                                                                   result_data[1]['location'])
    if tradeoff_factor == "cuisine":
        if len(tradeoff_data) > 0:
            if total_restaurants == 0:
                response += constants.response_tradeoff_no_restaurant.format(len(tradeoff_data),
                                                                             tradeoff_data[0]['cuisine'], "")
            else:
                response += constants.response_tradeoff.format(len(tradeoff_data), tradeoff_data[0]['cuisine'], "")
    else:
        if len(tradeoff_data) > 0:
            restaurant_tradeoff_type_str = ""
            if tradeoff_data[0][tradeoff_factor].lower() == "average":
                if tradeoff_factor == "price":
                    restaurant_tradeoff_type_str = "average priced"
                elif tradeoff_factor == "distance":
                    restaurant_tradeoff_type_str = "at an average distance"
            else:
                restaurant_tradeoff_type_str = tradeoff_data[0][tradeoff_factor]
            if total_restaurants == 0:
                response += constants.response_tradeoff_no_restaurant.format(len(tradeoff_data),
                                                                             "", "that are " + restaurant_tradeoff_type_str)
            else:
                response += constants.response_tradeoff.format(len(tradeoff_data),
                                                                             "", "that are " + restaurant_tradeoff_type_str)
    return response