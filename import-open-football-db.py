from itertools import izip
from pymongo.errors import BulkWriteError
from pprint import pprint
import pymongo
import glob
import os
import csv
import json


if __name__ == "__main__":
    db = pymongo.MongoClient().open_football

    print "parsing CSV'S"
    bulk_matches = db.matches_collection.initialize_ordered_bulk_op()
    matches = []
    for path, subdirs, files in os.walk("data/"):
        for name in files:
            for path, subdirs, files in os.walk("data"):
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
                                matches.append(match)

                                # exists = db.matches_collection.find(match)
                                # if exists.count() == 0:
                                
                                    
    try:
        print "Imported " + path
        bulk_matches.insert(matches)
        bulk_matches.execute()
    except BulkWriteError as bwe:
        pprint(bwe.details)