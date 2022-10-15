import random
import json

file = open('names.json')
data = json.load(file)


class Player:
    def __init__(self, pos):
        self.fname = random.choice(data['names'])
        self.lname = random.choice(data['names'])
        self.cap = random.randint(1, 50)
        self.age = random.randint(18, 31)
        self.pos = pos
        self.team_id = 1
        self.goals = random.randint(1, 50)
        self.games = self.cap + random.randint(1, 50)
        self.assists = self.goals + random.randint(1, 50)

    def incrTeamId():
        Player.team_id += 1
