import utils
import MySQLdb
import os
import MySQLdb.cursors


class DbConnection:
    def __init__(self):
        credentials = utils.dbcredentials(os.path.abspath(os.path.join(os.path.dirname(__file__))))
        self.connection = MySQLdb.connect(host=credentials["host"],  # your host, usually localhost
                                     user=credentials["user"],  # your username
                                     passwd=credentials["password"],  # your password
                                     db=credentials["db"],
                                     cursorclass=MySQLdb.cursors.SSDictCursor)  # stores result in the server. records as dict

    def get_cursor(self):
        return self.connection.cursor()