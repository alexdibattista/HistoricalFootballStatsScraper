import pymongo

client = pymongo.MongoClient()

#if 'openFootball' not in client.database_names():
db = client.open_football

exists = db.matches_collection.find({"HomeTeam": "Chievo",
"AwayTeam": "Juventus",})


match = {
"Div": "Serie A",
"Date": "30/08/14",
"HomeTeam": "Chievo",
"AwayTeam": "Juventus",
"FTHG": "0",
"FTAG": "1",
"FTR": "A",
"HTHG": "0",
"HTAG": "1",
"HTR": "A",
"HS": "7",
"AS": "21",
"HST": "2",
"AST": "3",
"HF": "13",
"AF": "14",
"HC": "4",
"AC": "11",
"HY": "2",
"AY": "1",
"HR": "0",
"AR": "0",
"B365H": "7",
"B365D": "4",
"B365A": "1.5",
"BWH": "6",
"BWD": "3.9",
"BWA": "1.55",
"IWH": "5.6",
"IWD": "3.9",
"IWA": "1.55",
"LBH": "6.5",
"LBD": "3.8",
"LBA": "1.53",
"PSH": "7.75",
"PSD": "4.12",
"PSA": "1.54",
"WHH": "6",
"WHD": "4",
"WHA": "1.55",
"SJH": "7",
"SJD": "3.75",
"SJA": "1.5",
"VCH": "8",
"VCD": "4",
"VCA": "1.53",
"Bb1X2": "49",
"BbMxH": "8",
"BbAvH": "7.01",
"BbMxD": "4.2",
"BbAvD": "3.9",
"BbMxA": "1.56",
"BbAvA": "1.53",
"BbOU": "47",
"BbMx": "2.11>2.5",
"BbAv": "1.98>2.5",
"BbMx": "1.89<2.5",
"BbAv": "1.8<2.5",
"BbAH": "27",
"BbAHh": "1",
"BbMxAHH": "2",
"BbAvAHH": "1.94",
"BbMxAHA": "1.98",
"BbAvAHA": "1.9"
}

if exists.count() == 0:
  matches = db.matches_collection
  matches.save(match)


print exists.count()

