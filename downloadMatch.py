import urllib3
import re
import ast

urllib3.disable_warnings(
    urllib3.exceptions.InsecureRequestWarning
)  #we do not check the certs of the resultssite, because it is not important enouogh for such a project.

http = urllib3.PoolManager()


def download(URL):
    try:
        r = http.request(
            'GET',
            URL,
            headers={
                'User-Agent':
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
            })  #get the actual site
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


teams = download(
    'https://www.whoscored.com/Regions/252/Tournaments/2/Seasons/7361/Stages/16368/TeamStatistics/'
)
teams = re.split(r'DataStore.prime', teams, 1)[1]
teams = re.split(r';', teams, 1)[0]
teams = re.split(',', teams)[6:]
teams = ','.join(teams)
teams = teams[:-1]
teams = teams.lstrip()
teams = ast.literal_eval(teams)[0]

for team in teams:
    teamID = team[0]
    teamName = team[1]

teamNames = dict()
teamNames['Manchester City'] = 'Manchester City'
teamNames['Liverpool'] = 'Liverpool'
teamNames['Chelsea'] = 'Chelsea'
teamNames['Newcastle United'] = 'Newcastle United'
teamNames['Tottenham'] = 'Tottenham Hotspur'
teamNames['Arsenal'] = 'Arsenal'
teamNames['Manchester United'] = 'Manchester United'
teamNames['Wolverhampton Wanderers'] = 'Wolverhampton Wanderers'
teamNames['Leicester'] = 'Leicester City'
teamNames['Watford'] = 'Watford'
teamNames['Everton'] = 'Everton'
teamNames['West Ham'] = 'West Ham United'
teamNames['Crystal Palace'] = 'Crystal Palace'
teamNames['Bournemouth'] = 'Bournemouth'
teamNames['Burnley'] = 'Burnley'
teamNames['Southampton'] = 'Southampton'
teamNames['Brighton'] = 'Brighton & Hove Albion'
teamNames['Cardiff'] = 'Cardiff City'
teamNames['Fulham'] = 'Fulham'
teamNames['Huddersfield'] = 'Huddersfield Town'
