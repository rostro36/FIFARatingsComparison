import urllib3
import re

urllib3.disable_warnings(
    urllib3.exceptions.InsecureRequestWarning
)  #we do not check the certs of the resultssite, because it is not important enouogh for such a project.

http = urllib3.PoolManager()


def download(URL):
    try:
        r = http.request('GET', URL)  #get the actual site
    except Exception as ex:
        print(ex)
        print('Internet not working.')
        quit()
    page = r.data.decode('UTF-8')
    return page


def getName(player):
    NAME = ''
    while player[0] != '(':
        NAME += player[0]
        player = player[1:]
    #delete trailing spaces
    return NAME.rstrip().lstrip()


matches = download('https://www.skysports.com/premier-league-results/2018-19')
matches = re.split(r'fixres matches', matches, 1)[1]
matches = re.split(r'Show More', matches, 1)[0]
matches = re.split(r'a href="', matches)[1:]

for match in matches:
    MATCHLINK = re.split(r'"', match)[0]
    firstTeam = re.split(r'football/', MATCHLINK, 1)[1]
    firstTeam = re.split(r'-vs-', firstTeam, 1)[0]
    print(firstTeam)
    secondTeam = re.split(r'-vs-', MATCHLINK, 1)[1]
    secondTeam = re.split(r'/', secondTeam, 1)[0]
    print(secondTeam)
    matchPage = download(MATCHLINK)
    firstTPlayers = re.split(r'</b>', matchPage)[1:3]
    firstTPlayers = ','.join(firstTPlayers)
    firstTPlayers = re.split(r',', firstTPlayers)
    print(firstTPlayers)
    for player in firstTPlayers:
        if '(' in player:
            NAME = getName(player)
            player = re.split(r'\(', player, 1)[1]
            GRADE = player[0]
        print(NAME)
        print(GRADE)
    secondTPlayers = re.split(r'</b>', matchPage)[3:5]
    secondTPlayers = ','.join(secondTPlayers)
    secondTPlayers = re.split(r',', secondTPlayers)
    print(secondTPlayers)
    for player in secondTPlayers:
        if '(' in player:
            NAME = getName(player)
            player = re.split(r'\(', player, 1)[1]
            GRADE = player[0]
            print(NAME)
            print(GRADE)

teamNames = dict()
teamNames['man-city'] = 'Manchester City'
teamNames['liverpool'] = 'Liverpool'
teamNames['chelsea'] = 'Chelsea'
teamNames['tottenham'] = 'Tottenham Hotspur'
teamNames['arsenal'] = 'Arsenal'
teamNames['man-utd'] = 'Manchester United'
teamNames['wolves'] = 'Wolverhampton Wanderers'
teamNames['leicester'] = 'Leicester City'
teamNames['watford'] = 'Watford'
teamNames['everton'] = 'Everton'
teamNames['west-ham'] = 'West Ham United'
teamNames['c-palace'] = 'Crystal Palace'
teamNames['bmouth'] = 'Bournemouth'
teamNames['burnley'] = 'Burnley'
teamNames['soton'] = 'Southampton'
teamNames['brighton'] = 'Brighton & Hove Albion'
teamNames['soton'] = 'Southampton'
teamNames['cardiff'] = 'Cardiff City'
teamNames['fulham'] = 'Fulham'
teamNames['huddsfld'] = 'Huddersfield Town'
