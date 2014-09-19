import pymongo
import glob
import os
import csv, json 

client = pymongo.MongoClient()

#if 'openFootball' not in client.database_names():
db = client.open_football

exists = db.matches_collection.find({"HomeTeam": "Chievo",
"AwayTeam": "Juventus"})


match = {
"Div": "{}",
"Date": "{}",
"HomeTeam": "{}",
"AwayTeam": "{}",
"FTHG": "{}",
"FTAG": "{}",
"FTR": "{}",
"HTHG": "{}",
"HTAG": "{}",
"HTR": "{}",
"HS": "{}",
"AS": "{}",
"HST": "{}",
"AST": "{}",
"HF": "{}",
"AF": "{}",
"HC": "{}",
"AC": "{}",
"HY": "{}",
"AY": "{}",
"HR": "{}",
"AR": "{}",
"B365H": "{}",
"B365D": "{}",
"B365A": "{}",
"BWH": "{}",
"BWD": "{}",
"BWA": "{}",
"IWH": "{}",
"IWD": "{}",
"IWA": "{}",
"LBH": "{}",
"LBD": "{}",
"LBA": "{}",
"PSH": "{}",
"PSD": "{}",
"PSA": "{}",
"WHH": "{}",
"WHD": "{}",
"WHA": "{}",
"SJH": "{}",
"SJD": "{}",
"SJA": "{}",
"VCH": "{}",
"VCD": "{}",
"VCA": "{}",
"Bb1X2": "{}",
"BbMxH": "{}",
"BbAvH": "{}",
"BbMxD": "{}",
"BbAvD": "{}",
"BbMxA": "{}",
"BbAvA": "{}",
"BbOU": "{}",
"BbMx": "{}",
"BbAv": "{}",
"BbMx": "{}",
"BbAv": "{}",
"BbAH": "{}",
"BbAHh": "{}",
"BbMxAHH": "{}",
"BbAvAHH": "{}",
"BbMxAHA": "{}",
"BbAvAHA": "{3}"
}

# if exists.count() == 0:
#   matches = db.matches_collection
#   matches.save(match)
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
for path, subdirs, files in os.walk("data"):
    for name in files:
        for path, subdirs, files in os.walk("data"):
            for name in files:
                print name + path
                with open(os.path.join(path, name), 'rb') as csvfile:
                    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
                    headers = next(reader)
                    out = [dict(zip(headers, property)) for property in reader]
                    print json.dumps(out)
                    # for index, row in enumerate(reader):
                    #     print headers

