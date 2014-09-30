#!/usr/bin/python
from bs4 import BeautifulSoup
from progressbar import ProgressBar
import urllib2
import re
import os
import argparse
import time


def chunk_report(pbar, bytes_so_far, chunk_size, total_size):
  value = float(bytes_so_far) / total_size
  # do something
  time.sleep(0.001)
  pbar.update(value + 1)


def chunk_read(pbar, response, chunk_size=8192, report_hook=None):
    total_size = response.headers['Content-Length']
    total_size = int(total_size)
    bytes_so_far = 0

    while 1:
        chunk = response.read(chunk_size)
        bytes_so_far += len(chunk)

        if not chunk:
            break

        if report_hook:
            report_hook(pbar, bytes_so_far, chunk_size, total_size)

    return bytes_so_far

def getLeagueContents(url, leagueUrl, args):
    html = getUrlContents(url + leagueUrl, args)
    bs = BeautifulSoup(html)

    tables = bs.findAll('td', valign="top")

    for table in tables:
        anchors = table.findAll("a")

        folderTitles = table.find("b")
        if folderTitles:
            for folderTitle in folderTitles:
                if "Data" in folderTitle:
                    folderTitle = re.sub('Data Files: ', '', folderTitle)

                if not os.path.exists("data/" + str(folderTitle)):
                    os.makedirs("data/" + str(folderTitle))

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

                    path = "data/" + folderTitle + "/" + anchor.text  + "/" + FirstPartOfYear + "-" + SecondPartOfYear

                    if not os.path.exists(path):
                        os.makedirs(path)

                    csvfilepath = path + "/" + anchor['href'].split('/')[2]

                    if not os.path.isfile(csvfilepath) and not os.access(csvfilepath, os.R_OK):
                        response = urllib2.urlopen(url + anchor['href'])

                    print anchor.text  + " " + FirstPartOfYear + "-" + SecondPartOfYear + " " + csvfilepath

                    # broken download progressbar
                    # with ProgressBar(widgets=[Percentage(), Bar()], maxval=10) as progress:
                    #   chunk_read(progress, response, report_hook=chunk_report)

                    with open(csvfilepath, "wb") as code:
                        code.write(response.read())

def getUrlContents(url, args):
    if args.p:
        proxies = {'http': 'http://142.174.134.33:8080'}
        response = urllib2.urlopen(url, proxies=proxies)
    else:
        response = urllib2.urlopen(url)

    html = response.read()

    return html

def main(url, args):
    html = getUrlContents(url + "data.php", args)
    bs = BeautifulSoup(html)
    rows = bs.find("table",  cellspacing="2", border="0").findChildren(['th', 'tr'])

    for row in rows:
        cells = row.findChildren('td')
        for cell in cells:
            value = cell.a
            if value:
                getLeagueContents(url, value['href'], args)


def arguments():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", action="store_true", default=False)
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    url = "http://football-data.co.uk/"
    dataUrl = "data.php"
    args = arguments()
    main(url, args)