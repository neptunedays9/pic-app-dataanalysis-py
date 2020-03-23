#!/usr/bin/python

from MySQLInterface import MySQLInterface
from SensitivityAnalysis import SensitivityAnalysis

def main():
        print("In main")
        raw = MySQLInterface.read()
        sensitivity = SensitivityAnalysis.process(raw)

if __name__ == '__main__':
    main()

# def test():
#     from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
#     analyzer = SentimentIntensityAnalyzer()
#     vs = analyzer.polarity_scores("he stopped speaking")
#     print(str(vs))
#     print(str(vs["compound"]))
#
#
#     # Open database connection
#     db = MySQLdb.connect("localhost","picuser","picuser123","pic_db" )
#
#     # prepare a cursor object using cursor() method
#     cursor = db.cursor()
#     cursor1 = db.cursor(MySQLdb.cursors.DictCursor)
#     # execute SQL query using execute() method.
#     cursor.execute("SELECT VERSION()")
#
#     # Fetch a single row using fetchone() method.
#     data = cursor.fetchone()
#     print ("Database version : %s " %data)
#
#     # execute SQL query using execute() method.
#     cursor1.execute("SELECT * from scene")
#
#     # Fetch a single row using fetchone() method.
#     data = cursor1.fetchall()
#     # print ("Database version : %s " %data)
#
#     for row in data:
#         print (row["scene"])
#         vs = analyzer.polarity_scores(row["scene"])
#         print(str(vs))
#
#     # disconnect from server
#     db.close()
