#!/usr/bin/python
import pymongo

def main():
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


if __name__ == '__main__':
    main()