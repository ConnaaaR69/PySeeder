# How to use this file
# Step 1: Create and click into the players table in phpmyadmin
# Step 2: Click import
# Step 3: Choose players.csv file in file browser
# Step 5: Paste the following column names into the "Column names" box: f_name,l_name,position,cap,age

import csv
import json
import random
import pymysql
import os
from classes.Player import Player

pNum = input(
    'Enter number of TEAMS to generate. There are 11 players per team. \n')
pNum = int(pNum)

cnx = pymysql.connect(user='root', password='',
                      host='localhost',
                      database='wcdb')

# Create a cursor
cursor = cnx.cursor()

# Randomly selects from lists and combines
# 'playernumber' arg can be changed to alter the number of entries generated


def randPlayers(playerNumber=pNum):
    test = "SELECT max(team_id) FROM players"
    cursor.execute(test)
    print(cursor.fetchmany())

    print('Generating Players')

    positions = ["Goalkeeper", "Right Back", "Left Back", "Center Back", "Sweeper",
                 "Defensive Midfield", "Right Wing", "Center Midfield", "Striker", "Center Forward", "Left Wing"]
    i = 0
    posCounter = 0
    team_id = 1

    while i < playerNumber:
        # Generate player
        player = Player(positions[posCounter], team_id)

        # create sql query to insert player to db
        query = "INSERT INTO players (first_name, last_name, age, cap, pos, goals_scored, games_played, assists, team_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %d)"

        # run sql query
        cursor.execute(query, (player.fname, player.lname, player.age, player.cap,
                       player.pos, player.goals, player.games, player.assists, player.team_id))

        cnx.commit()
        # player_list.append(player.getAll())

        # print(' Made player: {}'.format(vars(player)))

        # iteratives
        posCounter += 1

        # Reset Positions and increment team
        if(posCounter >= len(positions)):
            posCounter = 0
            team_id += 1
            i += 1


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
if(pNum > 10):
    os.system('cls||clear')
    sanityCheck = input(
        '{} entities will be created. Are you sure? Type \'Y\' to continue or any other entry to escape. \n'.format(pNum * 11))

    if(sanityCheck.upper() == 'Y'):
        randPlayers()
    else:
        print(sanityCheck)
        print('Aborting...')
        quit()
else:
    randPlayers()


# randStaff()


# # Writes to players.csv
# with open("data/players.csv", "w") as play:
#     # Sets delimitation and line terminations for CSV file
#     player = csv.writer(
#         play,
#         delimiter=",",
#         quotechar='"',
#         quoting=csv.QUOTE_ALL,
#         lineterminator='\r')

#     # Writes player_list array to file
#     player.writerows(player_list)
# # Output how many entries were created, from array len
# print('Created {} entries in players.csv'.format(len(player_list)))


# # Writes to staff.csv
# with open("data/staff.csv", "w") as wtr:
# Sets delimitation and line terminations for CSV file
# staff = csv.writer(
#     wtr,
#     delimiter=",",
#     quotechar='"',
#     quoting=csv.QUOTE_ALL,
#     lineterminator='\r')
# # Writes player_list array to file
# staff.writerows(staff_list)
