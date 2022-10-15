# How to use this file
# Step 1: Create and click into the players table in phpmyadmin
# Step 2: Click import
# Step 3: Choose players.csv file in file browser
# Step 5: Paste the following column names into the "Column names" box: f_name,l_name,position,cap,age

import csv
import json
import random
import os
from classes.Player import Player

pNum = input(
    'Enter number of players to generate. There are 11 players per team. \n')
pNum = int(pNum)


# Randomly selects from lists and combines
# 'playernumber' arg can be changed to alter the number of entries generated


def randPlayers(playerNumber=pNum):

    print('Generating Players')

    positions = ["Goalkeeper", "Right Back", "Left Back", "Center Back", "Sweeper",
                 "Defensive Midfield", "Right Wing", "Center Midfield", "Striker", "Center Forward", "Left Wing"]
    i = 0
    posCounter = 0
    team_id = 1

    while i < playerNumber:

        player = Player(pos=positions[posCounter])
        playerItrArr = [
            player.fname,
            player.lname,
            player.pos,
            player.team_id,
            player.cap,
            player.goals,
            player.games,
            player.assists,
            player.age]
        player_list.append(playerItrArr)

        # iterate
        i += 1
        posCounter += 1
        if(i % 11 == 0):
            team_id += 1
        if(posCounter >= len(positions)):
            posCounter = 0


def randStaff(staffNumber=100):
    print('--- Generated Staff Names ---')
    print(
        'fname' + ' ' +
        'lname' + ' ' +
        'position')
    print('-----------------------')
    i = 0
    posCounter = 0
    positions = ["Ticket Seller", "Janitor", "Water Person", "Physio", "Medic"]
    while i < staffNumber:
        # id = i + 1

        file = open('names.json')
        data = json.load(file)
        fname = random.choice(data['names'])
        lname = random.choice(data['names'])
        position = positions[posCounter]

        temp = [
            fname,
            lname,
            position]

        staff_list.append(temp)
        print(
            fname + ' ' +
            lname + ' ' +
            position)

        i += 1
        posCounter += 1
        if(posCounter >= len(positions)):
            posCounter = 0


# player
player_list = []
staff_list = []
if(pNum > 250):
    os.system('cls||clear')
    sanityCheck = input(
        '{} entries will be created. Are you sure? Type \'Y\' to continue or any other entry to escape. \n'.format(pNum))
else:
    randPlayers()
if(sanityCheck == 'Y'):
    randPlayers()
else:
    quit()
# randStaff()


# Writes to players.csv
with open("data/players.csv", "w") as play:
    # Sets delimitation and line terminations for CSV file
    player = csv.writer(
        play,
        delimiter=",",
        quotechar='"',
        quoting=csv.QUOTE_ALL,
        lineterminator='\r')

    # Writes player_list array to file
    player.writerows(player_list)
# Output how many entries were created, from array len
print('Created {} entries in players.csv'.format(len(player_list)))


# Writes to staff.csv
with open("data/staff.csv", "w") as wtr:
    # Sets delimitation and line terminations for CSV file
    staff = csv.writer(
        wtr,
        delimiter=",",
        quotechar='"',
        quoting=csv.QUOTE_ALL,
        lineterminator='\r')
    # Writes player_list array to file
    staff.writerows(staff_list)
