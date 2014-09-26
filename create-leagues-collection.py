#!/usr/bin/python
import pymongo


def find_unique_leagues():
    db = pymongo.MongoClient().open_football
    leagues = db.matches_collection.distinct("Div")
    return leagues





def main():
    leagues = find_unique_leagues()
    for league in leagues:
        
        # print leaguedb.matches_collection.find({$and:[{Date:{$gte: ISODate("2014-08-01"), $lte:ISODate("14-12-01")}}, { Div: "Serie A"} ]})

if __name__ == '__main__':
    main()
