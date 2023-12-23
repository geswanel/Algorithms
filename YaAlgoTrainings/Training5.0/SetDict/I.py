"""
Description:
Gather match stat and answer some questions related to that.
Match info format
    "command1" - "command2" score1:score2
    whoscored11 minute11'
    whoscored12 minute12'
    ...
    whoscored1score1 minute1score1'
    whoscored21 minute21'
    ...
    whoscored2score2 minute2score2'

Request types
    Total gols for Team
    Mean goals per game for Team
    Total goals by Player
    Mean goals per game by Player
    Goals on minute Min by Player   # exactly on Min
    Goals on first T minutes by Player  # from 1 to T min including
    Goals on last T minutes by Player  # from (91 - T) to 90 min including
    Score opens by Team     # how many times made a first goal
    Score opens by Player   # same for player
INPUT:
<= 100 matches. in each <= 10 goals. <= 20 teams. <= 10 players in each team scores
Any word length <= 30
min [1, 90] Only one goal for a minute in match
Requests <= 500
OUTPUT
For each request make a response

Solution:
class Team
    teamName: str
    totalScore: int
    gamesCnt: int
class Player
    name: str
    teamName: str
    goals: list

dict teamName: Team
dict playerName: Player
"""
import re


class Team:
    def __init__(self, teamName):
        self.teamName = teamName
        self.totalScore = 0
        self.totalGames = 0
        self.openings = 0
    
    def addGame(self, scored):
        self.totalScore += scored
        self.totalGames += 1
    
    def openScore(self):
        self.openings += 1
    
    def getOpenings(self):
        return self.openings
    
    def getTotalScore(self):
        return self.totalScore
    
    def getMeanScore(self):
        return round(self.totalScore / self.totalGames, 3)


class Player:
    def __init__(self, playerName, team: Team):
        self.playerName = playerName
        self.team = team
        self.goals = []
        self.openings = 0
    
    def score(self, minute):
        self.goals.append(minute)
        self.goals.sort()
    
    def openScore(self):
        self.openings += 1
    
    def getOpenings(self):
        return self.openings
    
    def getGoalsInRange(self, fr, to):
        ans = 0
        for goal in self.goals:
            if fr <= goal <= to:
                ans += 1
        
        return ans
    
    def getTotalGoals(self):
        return len(self.goals)
    
    def getMeanGoals(self):
        return round(len(self.goals) / self.team.totalGames, 3)

def processGoals(players: dict, team: Team, score: int, lines: list, stId: int):
    fGoalPlayer = None
    minMinute = 91
    for lId in range(stId, stId + score):
        match = re.match(r"([ a-zA-Z]+)(\d+)'", lines[lId])
        player = match.group(1).strip()
        minute = int(match.group(2))
        if player not in players:
            players[player] = Player(player, team)
        players[player].score(minute)

        if minute < minMinute:
            minMinute = minute
            fGoalPlayer = player

    return fGoalPlayer, minMinute

def processGame(teams: dict, players: dict, match: re.Match, lines: list, stId: int):
    team1, team2, s1, s2 = match.groups()
    s1 = int(s1)
    s2 = int(s2)
    if team1 not in teams:
        teams[team1] = Team(team1)
    if team2 not in teams:
        teams[team2] = Team(team2)
    teams[team1].addGame(s1); teams[team2].addGame(s2)

    fGoalPlayer1, min1 = processGoals(players, teams[team1], s1, lines, stId + 1)
    fGoalPlayer2, min2 = processGoals(players, teams[team2], s2, lines, stId + 1 + s1)

    if fGoalPlayer1 is not None or fGoalPlayer2 is not None:
        if min1 < min2:
            players[fGoalPlayer1].openScore()
            teams[team1].openScore()
        else:
            players[fGoalPlayer2].openScore()
            teams[team2].openScore()
    
    return stId + 1 + s1 + s2

def processRequest(teams: dict, players: dict, request: str):
    requestPatternId = {
        r'Total goals for (?P<tname>[ "a-zA-Z]+)': 0,
        r'Mean goals per game for (?P<tname>[ "a-zA-Z]+)': 1,
        r'Total goals by (?P<pname>[ a-zA-Z]+)': 2,
        r"Mean goals per game by (?P<pname>[ a-zA-Z]+)": 3,
        r"Goals on minute (?P<min>\d+) by (?P<pname>[ a-zA-Z]+)": 4,
        r"Goals on first (?P<min>\d+) minutes by (?P<pname>[ a-zA-Z]+)": 5,
        r"Goals on last (?P<min>\d+) minutes by (?P<pname>[ a-zA-Z]+)": 6,
        r'Score opens by (?P<name>[ "a-zA-Z]+)': 7
    }
    match = None
    id = -1
    for pattern, patId in requestPatternId.items():
        if match := re.match(pattern, request):
            id = patId
            break
    
    match id:
        case 0:
            team = teams.get(match.group("tname"), None)
            return team.getTotalScore() if team else 0
        case 1:
            team = teams.get(match.group("tname"), None)
            return team.getMeanScore() if team else 0
        case 2:
            player = players.get(match.group("pname"), None)
            return player.getTotalGoals() if player else 0
        case 3:
            player = players.get(match.group("pname"), None)
            return player.getMeanGoals() if player else 0
        case 4:
            player = players.get(match.group("pname"), None)
            minute = int(match.group("min"))
            return player.getGoalsInRange(minute, minute) if player else 0
        case 5:
            player = players.get(match.group("pname"), None)
            minute = int(match.group("min"))
            return player.getGoalsInRange(0, minute) if player else 0
        case 6:
            player = players.get(match.group("pname"), None)
            minute = int(match.group("min"))
            return player.getGoalsInRange(91 - minute, 90) if player else 0
        case 7:
            name = match.group("name")
            if name in players:
                return players[name].getOpenings()
            elif name in teams:
                return teams[name].getOpenings()
            else:
                return 0


def processData(filename: str, teams: dict, players: dict):
    with open(filename, 'r', encoding="utf-8") as f:
        lines = [line.rstrip() for line in f.readlines() if line.rstrip()]
    lId = 0
    while lId < len(lines):
        if (match := re.match(r'("[ a-zA-Z]+") - ("[ a-zA-Z]+") (\d+):(\d+)', lines[lId])):
            lId = processGame(teams, players, match, lines, lId)
        else:
            print(processRequest(teams, players, lines[lId]))
            lId += 1

def main():
    players = dict()
    teams = dict()
    processData("input.txt", teams, players)


if __name__ == "__main__":
    main()