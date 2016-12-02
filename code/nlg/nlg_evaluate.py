import confirm_action
import request_info
import response_action
import os
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
os.sys.path.insert(0, parentdir)
from data import constants
from include import db_conn


def evaluate_request_info():
    print "input: price" + "output: " + request_info.request_info('price')
    print "input: cuisine" + "output: " + request_info.request_info('cuisine')
    print "input: distance" + "output: " + request_info.request_info('distance')


def evaluate_confirm_action_all():
    for cuisine in constants.cuisine_keywords:
        for price in constants.price_keywords:
            for distance in constants.distance_keywords:
                print "input: %s %s %s" % (cuisine, price, distance)
                confirm_dict = {
                    'cuisine': cuisine,
                    'price': price,
                    'distance': distance
                }
                print "output: " + confirm_action.confirm_action_all(confirm_dict)


def evaluate_confirm_action_single():
    for cuisine in constants.cuisine_keywords:
        print "input: " + cuisine + " output: " + confirm_action.confirm_action_single({'cuisine': cuisine})
    for price in constants.price_keywords:
        print "input: " + price + " output: " + confirm_action.confirm_action_single({'price': price})
    for distance in constants.distance_keywords:
        print "input: " + distance + " output: " + confirm_action.confirm_action_single({'distance': distance})


def evaluate_response_action():
    db_connection = db_conn.DbConnection()
    for cuisine in constants.cuisine_keywords:
        for price in constants.price_keywords:
            for i in range(0, len(constants.distance_keywords)):
                query = "SELECT name, location, rating, cuisine, price, distance from restaurants where cuisine = '{}' and \
                distance = '{}' and price = '{}' ORDER BY rating DESC"
                cursor = db_connection.get_cursor()
                cursor.execute(query.format(cuisine, constants.distance_keywords[i], price))
                response_main = cursor.fetchall()
                cursor.close()
                if i == 0:
                    tradeoff = constants.distance_keywords[-1]
                else:
                    tradeoff = constants.distance_keywords[i - 1]
                cursor = db_connection.get_cursor()
                cursor.execute(query.format(cuisine, tradeoff, price))
                response_tradeoff = cursor.fetchall()
                cursor.close()
                print "input: %s %s %s" % (cuisine, price, constants.distance_keywords[i])
                print "output: " + response_action.response_action(response_main, 'distance', response_tradeoff)

    for cuisine in constants.cuisine_keywords:
        for distance in constants.distance_keywords:
            for i in range(0, len(constants.price_keywords)):
                query = "SELECT name, location, rating, cuisine, price, distance from restaurants where cuisine = '{}' and \
                distance = '{}' and price = '{}' ORDER BY rating DESC"
                cursor = db_connection.get_cursor()
                cursor.execute(query.format(cuisine, distance, constants.price_keywords[i]))
                response_main = cursor.fetchall()
                cursor.close()
                if i == 0:
                    tradeoff = constants.price_keywords[-1]
                else:
                    tradeoff = constants.price_keywords[i - 1]
                cursor = db_connection.get_cursor()
                cursor.execute(query.format(cuisine, distance, tradeoff))
                response_tradeoff = cursor.fetchall()
                cursor.close()
                print "input: %s %s %s" % (cuisine, constants.price_keywords[i], distance)
                print "output: " + response_action.response_action(response_main, 'price', response_tradeoff)

    for price in constants.price_keywords:
        for distance in constants.distance_keywords:
            for i in range(0, len(constants.cuisine_keywords)):
                query = "SELECT name, location, rating, cuisine, price, distance from restaurants where cuisine = '{}' and \
                distance = '{}' and price = '{}' ORDER BY rating DESC"
                cursor = db_connection.get_cursor()
                cursor.execute(query.format(constants.cuisine_keywords[i], distance, price))
                response_main = cursor.fetchall()
                cursor.close()
                if i == 0:
                    tradeoff = constants.cuisine_keywords[-1]
                else:
                    tradeoff = constants.cuisine_keywords[i - 1]
                cursor = db_connection.get_cursor()
                cursor.execute(query.format(tradeoff, distance, price))
                response_tradeoff = cursor.fetchall()
                cursor.close()
                print "input: %s %s %s" % (constants.cuisine_keywords[i], price, distance)
                print "output: " + response_action.response_action(response_main, 'cuisine', response_tradeoff)


# evaluate_request_info()
# evaluate_confirm_action_all()
# evaluate_confirm_action_single()
evaluate_response_action()