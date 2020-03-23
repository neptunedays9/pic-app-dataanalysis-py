#!/usr/bin/python
from MySQLInterface import MySQLInterface

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

class SensitivityAnalysis:
    def process(raw):
        print("In process", raw)
        # sensitivity = []
        analyzer = SentimentIntensityAnalyzer()
        for row in raw:
            print (row["scene"])
            vs = analyzer.polarity_scores(row["scene"])
            print(str(vs))
            MySQLInterface.write(row["id"], str(vs))

            # sensitivity.append(str(vs))
        # return sensitivity
