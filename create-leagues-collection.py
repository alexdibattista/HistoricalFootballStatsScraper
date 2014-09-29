#!/usr/bin/python
import datetime
import pymongo


def find_unique_leagues():
    db = pymongo.MongoClient().open_football
    # mongo equivalent  db.matches_collection.find({$and:[{Date:{$gte: new Date("08/01/2013"), $lte: new Date("08/01/2014")}}, { Div: "Serie A"} ]})
    start = datetime.datetime.strptime("01/08/13", "%d/%m/%y")
    end = datetime.datetime.strptime("01/07/14", "%d/%m/%y")

    leagues = db.matches_collection.find({"$and":[{"Date":{"$gte": start, "$lte": end}}, { "Div": "Serie A"} ]})
    return leagues





def main():

    leagues = find_unique_leagues()
    
    for match in leagues:
      print match 
      print "\n"

    print leagues.count()

if __name__ == '__main__':
    main()
    