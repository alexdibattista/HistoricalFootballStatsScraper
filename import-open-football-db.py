import pymongo
import glob
import os
import csv, json 

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
                    headers = next(reader)
                    
                    for line in reader:
                        if set(line).pop() != '':
                            out = [dict(zip(headers, line))]
                            matchJsonObj = json.dumps(out)

                            exists = db.matches_collection.find(matchJsonObj)
                            if exists.count() == 0:
                              matches = db.matches_collection
                              matches.save(matchJsonObj)