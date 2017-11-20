import requests, operator

class Team:
  def __init__(self, ID, fullName, abbreviation, squadValueEuros):
    self.ID = ID
    self.fullName = fullName
    self.abbreviation = abbreviation
    self.squadValueEuros = squadValueEuros
  
  def __str__(self):
    return "ID: %s\nFull Name: %s\nAbbreviation: %s\nMarket Value: %s" % (self.ID, self.fullName, self.abbreviation, self.squadValueEuros)

class Fixture:
  def __init__(self, ID, homeTeam, awayTeam, homeTeamScore, awayTeamScore):
    self.ID = ID
    self.homeTeam = homeTeam
    self.awayTeam = awayTeam
    self.homeTeamScore = homeTeamScore
    self.awayTeamScore = awayTeamScore
    
  def __str__(self):
    return "ID: %s\nHome team: %s\nAway team: %s\nHome team score: %s\nAway team score: %s" % (self.ID, self.homeTeam, self.awayTeam, self.homeTeamScore, self.awayTeamScore)
  
def constructLeagueTable(teamObjects, fixtureObjects):
  teamDict = {}
  for i in teamObjects:
    exec("teamDict[%s.fullName] = 0" % i)
    
  for i in fixtureObjects:
    exec("if %s.homeTeamScore > %s.awayTeamScore:\n\tteamDict[%s.homeTeam] += 3\nelif %s.homeTeamScore == %s.awayTeamScore:\n\tteamDict[%s.homeTeam] += 1\n\tteamDict[%s.awayTeam] += 1" % (i, i, i, i, i, i, i))
    
  sortedTeamList = sorted(teamDict.items(), key=operator.itemgetter(1))[::-1]
  
  for i in sortedTeamList:
    print(i[0] + " : " + str(i[1]))
  
r = requests.get("http://api.football-data.org/alpha/soccerseasons/449/teams", headers={"X-Auth-Token" : "0af119bae2c3411483ab2df3714b615b"}).json()
s = requests.get("http://api.football-data.org/alpha/soccerseasons/449/fixtures", headers={"X-Auth-Token" : "0af119bae2c3411483ab2df3714b615b"}).json()

teamObjects = []
fixtureObjects = []

for i in r["teams"]:
  ID = i["_links"]["self"]["href"][-3:]
  exec("team%s = Team(ID, i[\"name\"], i[\"shortName\"], i[\"squadMarketValue\"])" % ID)
  teamObjects.append("team%s" % ID)

for i in s["fixtures"]:
  ID = i["_links"]["self"]["href"][-6:]
  exec("fixture%s = Fixture(ID, i[\"homeTeamName\"], i[\"awayTeamName\"], i[\"result\"][\"goalsHomeTeam\"], i[\"result\"][\"goalsAwayTeam\"])" % ID)
  fixtureObjects.append("fixture%s" % ID)
  
constructLeagueTable(teamObjects, fixtureObjects)
