from bs4 import BeautifulSoup
import urllib
import re, os

url = "http://football-data.co.uk/"
dataUrl= "data.php"

def getLeagueContents(url, leagueUrl):
  html = getUrlContents(url + leagueUrl)
  bs = BeautifulSoup(html)

  tables = bs.findAll('td', valign="top")

  for table in tables:

      anchors = table.findAll("a")

      folderTitles = table.find("b")
      if folderTitles:
        for folderTitle in folderTitles:
          if "Data" in folderTitle:
            folderTitle = re.sub('Data Files: ', '', folderTitle)
            
            if not os.path.exists("data/" + folderTitle):
              os.makedirs("data/" + folderTitle)

      for anchor in anchors:
        if anchor:

          if "csv" in str(anchor['href']):

            FirstPartOfYear = anchor['href'].split('/')[1][0:2]
            SecondPartOfYear = anchor['href'].split('/')[1][2:]
            
            if "0" in str(FirstPartOfYear) or "1" in str(FirstPartOfYear):
              FirstPartOfYear = "20" + FirstPartOfYear
            else:
              FirstPartOfYear = "19" + FirstPartOfYear

            if "0" in str(SecondPartOfYear) or "1" in str(SecondPartOfYear):
              SecondPartOfYear = "20" + SecondPartOfYear
            else:
              SecondPartOfYear = "19" + SecondPartOfYear

            path = "data/" + folderTitle + "/" + anchor.text  + "/" + FirstPartOfYear + " " + SecondPartOfYear

            if not os.path.exists(path):
              os.makedirs(path)

            csvfilepath = path + "/" + anchor['href'].split('/')[2]

            if not os.path.isfile(csvfilepath) and not os.access(csvfilepath, os.R_OK):
              urllib.urlretrieve (url + anchor['href'], csvfilepath)

def getUrlContents(url):
  response = urllib.urlopen(url)
  html = response.read()

  return html


html = getUrlContents(url + "data.php")

bs = BeautifulSoup(html)

rows = bs.find("table",  cellspacing="2", border="0").findChildren(['th', 'tr'])

for row in rows:
  cells = row.findChildren('td')
  for cell in cells:
      value = cell.a
      if value:
        getLeagueContents(url, value['href'])
