import pymongo
import glob
import os
import csv, json
from itertools import izip

client = pymongo.MongoClient()

#if 'openFootball' not in client.database_names():
db = client.open_football

class UnicodeDictReader(csv.DictReader):
    def __init__(self, f, encoding, *args, **kwargs):
        csv.DictReader.__init__(self, f, *args, **kwargs)
        self.encoding = encoding
    def next(self):
        return {
            k.decode(self.encoding): v.decode(self.encoding)
            for (k, v) in csv.DictReader.next(self).items()
        }

print "parsing csvs"
for path, subdirs, files in os.walk("data/"):
    for name in files:
        for path, subdirs, files in os.walk("data/Belgium/Jupiler League/1995-1996/"):
            for name in files:
                print name + path
                with open(os.path.join(path, name), 'rb') as csvfile:
                    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
                    removeHeaders = next(reader)
                    headers = ['Div','Date','HomeTeam','AwayTeam','FTHG','FTAG','FTR','HTHG','HTAG','HTR','Referee','HS','AS','HST','AST', 'HF', 'AF', 'HC', 'AC', 'HY', 'AY', 'HR', 'AR','B365H','B365D','B365A','BWH','BWD','BWA','IWH','IWD','IWA','LBH','LBD','LBA','PSH','PSD','PSA','WHH','WHD','WHA','SJH','SJD','SJA','VCH','VCD','VCA','Bb1X2','BbMxH','BbAvH','BbMxD','BbAvD','BbMxA','BbAvA','BbOU','BbMx>2.5','BbAv>2.5','BbMx<2.5','BbAv<2.5','BbAH','BbAHh','BbMxAHH','BbAvAHH','BbMxAHA','BbAvAHA']

                    for line in reader:
                        if set(line).pop() != '':
                            matchList = iter(line)
                            out = dict(izip(headers, matchList))
                            print type(out)
                            

                            exists = db.matches_collection.find(out)
                            if exists.count() == 0:
                                print "doesn't exist"
                                # matches = db.matches_collection
                                # matches.save(matchJsonObj)