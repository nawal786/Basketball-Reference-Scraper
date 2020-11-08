'''
N. Valliani
Stats Scraper for Basketball-Reference.com
Version 1.1

v1.1 Changelog:
In all functions, added a column to the returned Pandas Dataframe to report the year of the data (season end year).
Cleaned up some stray unused code laying around from 1.0
'''

from bs4 import BeautifulSoup
import requests
import lxml
import pandas as pd
import sys
import datetime

now = datetime.datetime.now()

def terminateWithError(message):
    print(message)
    sys.exit()

def getPlayerList(letter):
    base = "https://www.basketball-reference.com/players"
    url = "{0}/{1}/".format(base,letter)

    # get the page source, print out url being retrieved
    obj = requests.get(url).text
    print("\n" + "*" * 100)
    print("Retrieving Data From: " + url)

    # BeautifulSoup can't read stuff in HTML comments, so remove all comment tags from source
    obj = obj.replace('<!--', '')
    obj = obj.replace('-->', '')

    if "Page Not Found (404 error)" in obj:
        terminateWithError("Terminating - 404 Page Not Found!")

    # Create the soup object and find the table with Totals
    soup = BeautifulSoup(obj, 'lxml')

    players = soup.find('table', id='players')
    tables = players.find('tbody')
    table_rows = tables.find_all('tr')

    print("*" * 100)

'''
Returns player's gamelog data for a given season for regular season or playoffs (i.e., home/away game, FG, FGA, FT, other per game performance data, etc.)

Inputs: 
Player's BKref identifier (e.g., Stephen Curry - curryst01, Kobe Bryant - bryanko1) - String Input
Season (e.g., for 2011-2012 season input 2012, for 2015-2016 season input 2016) - Integer Input
Option (enter 0 for regular season stats, any other integer for playoffs stats) - Integer Input

Outputs:
Pandas DataFrame
'''
def getGameStats(player,year,opt):

    if(year > now.year):
        terminateWithError("Cannot access data from {0}, because that's in the future. "
                           "The current year is {1}.".format(year,now.year))

    letter = player[0]
    base = "https://www.basketball-reference.com/players"
    url = "{0}/{1}/{2}/gamelog/{3}".format(base,letter,player,year)
    data = []

    # get the page source, print out url being retrieved
    obj = requests.get(url).text
    print("\n" + "*"*100)
    print("Retrieving Data From: " + url)

    # BeautifulSoup can't read stuff in HTML comments, so remove all comment tags from source
    obj = obj.replace('<!--', '')
    obj = obj.replace('-->', '')

    if "Page Not Found (404 error)" in obj:
        terminateWithError("Terminating - 404 Page Not Found!")

    # Create the soup object and find the table with Totals
    soup = BeautifulSoup(obj, 'lxml')

    title = str(soup.find('title'))
    title = title.replace("<title>","")
    title = title.split("|")
    player = title[0]

    if(opt == 0):
        gamelog = soup.find('table', id='pgl_basic')
        print("Retrieving Regular Season Stats - {0}".format(player))
    elif(opt != 0):
        gamelog = soup.find('table', id='pgl_basic_playoffs')
        print("Retrieving Playoff Stats - {0}".format(player))

    print("*"*100)
    tables = gamelog.find('tbody')
    table_rows = tables.find_all('tr')

    for tr in table_rows:

        td = tr.find_all('td')
        row = [i.text for i in td]

        if row:
            data.append(row)

    for i in range(len(data)):
        if "@" in data[i]:
            data[i][4] = "AWAY"
        else:
            data[i][4] = "HOME"

    col = ["G", "Date", "Age", "Tm", "Loc", "Opp", "W/L (PtsDiff)", "GS", "MP", "FG", "FGA", "FG%", "3P", "3PA", "3P%", "FT", "FTA",
           "FT%", "ORB", "DRB", "TRB", "AST", "STL", "BLK", "TOV", "PF", "PTS", "GmSc", "+/-"]

    data_DF = pd.DataFrame(data,columns = col)
    data_DF["Year (Season End)"] = year
    return data_DF

'''
Returns player's shooting stats for a given season for various splits (e.g., regular season/playoffs, 2s/3s, quarters, VS. teams, etc.)
Inputs: 
Player's BKref identifier (e.g., Stephen Curry - curryst01, Kobe Bryant - bryanko1) - String Input
Season (e.g., for 2011-2012 season input 2012, for 2015-2016 season input 2016) - Integer Input

Outputs:
Pandas DataFrame
'''
def getShootingStats(player,year):

    if(year > now.year):
        terminateWithError("Cannot access data from {0}, because that's in the future. "
                           "The current year is {1}.".format(year,now.year))

    letter = player[0]
    base = "https://www.basketball-reference.com/players"
    url = "{0}/{1}/{2}/shooting/{3}".format(base,letter,player,year)
    data = []

    # get the page source, print out url being retrieved
    obj = requests.get(url).text
    print("\n" + "*"*100)
    print("Retrieving Data From: " + url)

    # BeautifulSoup can't read stuff in HTML comments, so remove all comment tags from source
    obj = obj.replace('<!--', '')
    obj = obj.replace('-->', '')

    if "Page Not Found (404 error)" in obj:
        terminateWithError("Terminating - 404 Page Not Found!")

    # Create the soup object and find the table with Totals
    soup = BeautifulSoup(obj, 'lxml')

    title = str(soup.find('title'))
    title = title.replace("<title>","")
    title = title.split("|")
    player = title[0]

    print("Retrieving Shot Stats - {0}".format(player))

    shooting = soup.find('table', id='shooting')
    print("*"*100)
    table_rows = shooting.find_all('tr')

    for tr in table_rows:
        td = tr.find_all('td')
        row = [i.text for i in td]

        if row:
            data.append(row)

    col = ["Value", "FG", "FGA", "FG%", "3P", "3PA", "3P%", "eFG%", "Ast'd", "%Ast'd"]

    data_DF = pd.DataFrame(data,columns = col)
    data_DF["Year (Season End)"] = year
    return data_DF