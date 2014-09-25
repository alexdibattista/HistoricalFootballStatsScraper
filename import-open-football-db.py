from itertools import izip
from pymongo.errors import BulkWriteError
from pprint import pprint
import pymongo
import glob
import os
import csv
import json
import datetime

def import_leagues():
    db = pymongo.MongoClient().open_football
    #drop the old db
    db.matches_collection.drop()
    print "parsing CSV'S"
    bulk_matches = db.matches_collection.initialize_ordered_bulk_op()
    matches = []

    for path, subdirs, files in os.walk("data/"):
        for name in files:
            print path
            
            with open(os.path.join(path, name), 'rb') as csvfile:
                reader = csv.reader(csvfile, delimiter=',', quotechar='|')
                removeHeaders = next(reader)
                headers = ['Div','Date','HomeTeam','AwayTeam','FTHG','FTAG','FTR','HTHG','HTAG','HTR','Referee','HS','AS','HST','AST', 'HF', 'AF', 'HC', 'AC', 'HY', 'AY', 'HR', 'AR','B365H','B365D','B365A','BWH','BWD','BWA','IWH','IWD','IWA','LBH','LBD','LBA','PSH','PSD','PSA','WHH','WHD','WHA','SJH','SJD','SJA','VCH','VCD','VCA','Bb1X2','BbMxH','BbAvH','BbMxD','BbAvD','BbMxA','BbAvA','BbOU','BbMx>2_5','BbAv>2_5','BbMx<2_5','BbAv<2_5','BbAH','BbAHh','BbMxAHH','BbAvAHH','BbMxAHA','BbAvAHA']

                for line in reader:
                    if set(line).pop() != '':
                        matchList = iter(line)
                        match = dict(izip(headers, matchList))

                        bulk_matches.insert(match)

                        # exists = db.matches_collection.find(match)
                        # if exists.count() == 0:
            
    try:
        print "Imported data"
        bulk_matches.execute()
    except BulkWriteError as bwe:
        pprint(bwe.details)

def change_league_names():
    print "Updating League Names"
    db = pymongo.MongoClient().open_football
    bulk = db.matches_collection.initialize_ordered_bulk_op()
    bulk.find({ "Div":"E0"}).update({ "$set": {"Div": "Barclays Premier League" }})
    bulk.find({ "Div":"E1"}).update({ "$set": {"Div": "Football League Championship" }})
    bulk.find({ "Div":"E1"}).update({ "$set": {"Div": "League 1" }})
    bulk.find({ "Div":"E2"}).update({ "$set": {"Div": "League 2" }})
    bulk.find({ "Div":"E3"}).update({ "$set": {"Div": "League 3" }})
    bulk.find({ "Div":"B1"}).update({ "$set": {"Div": "Jupiler League" }})
    bulk.find({ "Div":"F1"}).update({ "$set": {"Div": "Ligue 1" }})
    bulk.find({ "Div":"F2"}).update({ "$set": {"Div": "Ligue 2" }})
    bulk.find({ "Div":"D1"}).update({ "$set": {"Div": "Bundesliga" }})
    bulk.find({ "Div":"D2"}).update({ "$set": {"Div": "Bundesliga 2" }})
    bulk.find({ "Div":"G1"}).update({ "$set": {"Div": "Super League Greece" }})
    bulk.find({ "Div":"I1"}).update({ "$set": {"Div": "Serie A" }})
    bulk.find({ "Div":"I2"}).update({ "$set": {"Div": "Serie B" }})
    bulk.find({ "Div":"N1"}).update({ "$set": {"Div": "EreDivisie" }})
    bulk.find({ "Div":"P1"}).update({ "$set": {"Div": "Primeira Liga" }})
    bulk.find({ "Div":"SC0"}).update({ "$set": {"Div": "Scottish Premier League" }})
    bulk.find({ "Div":"SC1"}).update({ "$set": {"Div": "Scottish League 1" }})
    bulk.find({ "Div":"SC2"}).update({ "$set": {"Div": "Scottish League 2" }})
    bulk.find({ "Div":"SC3"}).update({ "$set": {"Div": "Scottish League 3" }})
    bulk.find({ "Div":"SP1"}).update({ "$set": {"Div": "La Liga Primera Division" }})
    bulk.find({ "Div":"SP2"}).update({ "$set": {"Div": "La Liga Segunda Division" }})
    bulk.find({ "Div":"T1"}).update({ "$set": {"Div": "Futbol Ligi 1 " }})
    bulk.execute()


def update_match_string_date_to_datetime():
    print "Updating Match Dates"
    db = pymongo.MongoClient().open_football
    # cursor = db.matches_collection.find()
    matches = db.matches_collection.find()
    bulk = db.matches_collection.initialize_ordered_bulk_op()

    # while (next(cursor, None)):
    #     doc = cursor.next();
    #     try:
    #         date = datetime.datetime.strptime(doc["Date"], "%d/%m/%y")
    #     except Exception, e:
    #         date = datetime.datetime.strptime(doc["Date"], "%d/%m/%Y")

    #     db.matches_collection.update({"Date" : doc["Date"]}, {"$set" : {"Date" : date}})

    for match in matches:
        try:
            date = datetime.datetime.strptime(match["Date"], "%d/%m/%y")
        except Exception, e:
            date = datetime.datetime.strptime(match["Date"], "%d/%m/%Y")

        bulk.find({"_id": match["_id"]}).update({'$set': {'Date': date.strftime('%m/%d/%Y')}})

    bulk.execute()


if __name__ == "__main__":
    import_leagues()
    change_league_names()
    update_match_string_date_to_datetime()