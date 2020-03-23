#!/usr/bin/python

import MySQLdb

class MySQLInterface:
    def read():

        # Open database connection
        db = MySQLdb.connect("localhost","picuser","picuser123","pic_db" )

        # prepare a cursor object using cursor() method
        cursor = db.cursor(MySQLdb.cursors.DictCursor)

        # execute SQL query using execute() method.
        cursor.execute("SELECT * from scene")

        # Fetch a single row using fetchone() method.
        data = cursor.fetchall()
        print("In read", data)

        # disconnect from server
        db.close()

        return data


    def write(id, data):
        print("In write", id, data)

        # Open database connection
        db = MySQLdb.connect("localhost","picuser","picuser123","pic_db" )

        # prepare a cursor object using cursor() method
        cursor = db.cursor(MySQLdb.cursors.DictCursor)

        # execute SQL query using execute() method.
        cursor.execute('INSERT IGNORE into Sensitivity VALUES(%s)', data["neg"])

        # disconnect from server
        db.close()
