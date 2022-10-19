import random
import json

file = open('names.json')
data = json.load(file)


class Player:
    def __init__(self, pos, team_id):
        self.fname = random.choice(data['names'])
        self.lname = random.choice(data['names'])
        self.cap = random.randint(1, 50)
        self.age = random.randint(18, 31)
        self.pos = pos
        self.team_id = team_id
        self.goals = random.randint(1, 50)
        self.games = self.cap + random.randint(1, 50)
        self.assists = self.goals + random.randint(1, 50)

    def getAll(self):
        selfArr = [self.fname,
                   self.lname,
                   self.pos,
                   self.team_id,
                   self.cap,
                   self.goals,
                   self.games,
                   self.assists,
                   self.age]
        return selfArr
