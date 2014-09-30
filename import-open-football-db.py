#!/usr/bin/python
from itertools import izip
from pprint import pprint
from pymongo.errors import BulkWriteError

import codecs
import csv
import datetime
import os
import pymongo

def import_leagues():
    db = pymongo.MongoClient().open_football
    #drop the old db
    print "Drop old DB"
    db.matches_collection.drop()
    print "parsing CSV'S"
    bulk_matches = db.matches_collection.initialize_ordered_bulk_op()
    matches = []
    record = 0
    missed = 0
    
    for path, subdirs, files in os.walk("data"):
        for name in files:
            # print path
            record = 0
            with open(os.path.join(path, name), 'rb') as csvfile:
                try:

                #     dialect = csv.Sniffer().sniff(csvfile.read(1024), delimiters=",")
                #     # Perform various checks on the dialect (e.g., lineseparator,
                #     # delimiter) to make sure it's sane

                #     # Don't forget to reset the read position back to the start of
                #     # the file before reading any entries.
                #     print "CSV"
                #     csvfile.seek(0)

                    reader = csv.reader(csvfile, delimiter=",", quotechar='|') 

                    next(reader)  # skip header row

                    headers = ['Div','Date','HomeTeam','AwayTeam','FTHG','FTAG','FTR','HTHG','HTAG','HTR','Referee','HS','AS','HST','AST', 'HF', 'AF', 'HC', 'AC', 'HY', 'AY', 'HR', 'AR','B365H','B365D','B365A','BWH','BWD','BWA','IWH','IWD','IWA','LBH','LBD','LBA','PSH','PSD','PSA','WHH','WHD','WHA','SJH','SJD','SJA','VCH','VCD','VCA','Bb1X2','BbMxH','BbAvH','BbMxD','BbAvD','BbMxA','BbAvA','BbOU','BbMx>2_5','BbAv>2_5','BbMx<2_5','BbAv<2_5','BbAH','BbAHh','BbMxAHH','BbAvAHH','BbMxAHA','BbAvAHA']
                    

                    for idx, line in enumerate(reader):
                        matchList = iter(line)
                        match = dict(izip(headers, matchList))
                        
                        if line or not line.strip() == "" or ''.join(line.split(',')).strip() == '':
                            # if set(line).pop() == '':
                            #     print "passed:" + str(idx) + ":" + match["HomeTeam"] + " " + match["AwayTeam"]
                            #     missed +=1
                            # else:
                            try:
                                match["Date"] = datetime.datetime.strptime(match["Date"], "%d/%m/%y")
                            except Exception, e:
                                match["Date"] = datetime.datetime.strptime(match["Date"], "%d/%m/%Y")

                            record += 1
                            bulk_matches.insert(match)
                        else:
                            missed +=1
                            print str(idx) + ":" + match["HomeTeam"] + " " + match["AwayTeam"]

                except:
                    # print err
                    pass

            print str(os.path.join(path, name)) + str(record)
    
    print "Imported data"
    result = bulk_matches.execute()
    print missed
    pprint(result)
    


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

if __name__ == "__main__":
    import_leagues()
    change_league_names()