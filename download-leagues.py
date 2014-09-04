from bs4 import BeautifulSoup
import urllib

url = "http://football-data.co.uk/"
dataUrl= "data.php"
file = open("newfile.txt", "w")

def getLeagueContents(url):
  html = getUrlContents(url)
  bs = BeautifulSoup(html)

  tables = bs.findAll('td', valign="top")
  for table in tables:
      titles = table.findAll("i")

      for title in titles:
        if not "Last" in str(title):
          print title

      anchors = table.findAll("a")
      for anchor in anchors:
        if anchor:
          if "csv" in str(anchor['href']):
            print anchor['href'].split('/')[1]

     
  #file.write(str(tables) + "\n")

  # for table in tables:
  #   rows = table.findChildren('tr')
  #   for row in rows:
  #     cells = row.findChildren('td')
  #     for cell in cells:
  #       value = cell.a
  #       if value:
  #         file.write(str(value) + "\n")

def getUrlContents(url):
  response = urllib.urlopen(url)
  html = response.read()

  return html


html = getUrlContents(url + "data.php")

bs = BeautifulSoup(html)

rows = bs.find("table",  cellspacing="2", border="0").findChildren(['th', 'tr'])

#for row in rows:
cells = rows[0].findChildren('td')
for cell in cells:
    value = cell.a
    if value:
      getLeagueContents(url + value['href'])

file.close()