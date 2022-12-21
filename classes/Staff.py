import random
import json

file = open('names.json')
data = json.load(file)


class Staff:
    def __init__(self, pos, team_id):
        self.fname = random.choice(data['names'])
        self.lname = random.choice(data['names'])
        self.pos = pos
        self.team_id = team_id

    def getAll(self):
        selfArr = [self.fname,
                   self.lname,
                   self.pos,
                   self.team_id]
        return selfArr
