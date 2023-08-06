#!/usr/bin/python3

"""Script that lists all 'states' from the database 'hbtn_0e_0_usa'"""

import MySQLdb
import sys

def list_states(username, password, db_name):
    """Function to list a table
       Args:
       username: Username
       password: Password
       db_name: Database name
    """
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=username, passwd=password, db=db_name)

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()


if __name__ == "__main__":
    """Code block that is executed when the file is executed directly"""
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    list_states(username, password, db_name)
