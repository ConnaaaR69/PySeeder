# How to use this file
# Step 0: Change db credentials
# Step 1: run this file using the command 'py seed.py'
# Step 2: Input number of teams
# Step 3: Bask in its glory!


import json
import random
import pymysql
import os
from classes.Player import Player
from classes.Staff import Staff

###############################
# Change these variables to your db credentials
# no other changes to this file are required.

USERNAME = 'root'
PASSWORD = ''
HOST = 'localhost'
DATABASE = 'wcdb'

###############################


pNum = input(
    'Enter number of TEAMS to generate. There are 11 players per team. \n')
pNum = int(pNum)

cnx = pymysql.connect(user=USERNAME, password=PASSWORD,
                      host=HOST,
                      database=DATABASE)

# Create a cursor
cursor = cnx.cursor()


def randPlayers(playerNumber=pNum):

    # THIS WILL EMPTY TABLE BEFORE SEEDING
    clear = "TRUNCATE TABLE `{}`.`players`".format(DATABASE)
    cursor.execute(clear)

    print('Generating Players')

    positions = ["Goalkeeper", "Right Back", "Left Back", "Center Back", "Sweeper",
                 "Defensive Midfield", "Right Wing", "Center Midfield", "Striker", "Center Forward", "Left Wing"]

    # init variables
    i = 0
    posCounter = 0
    team_id = 1

    while i < playerNumber:
        # Generate player
        player = Player(positions[posCounter], team_id)

        # create sql query to insert player to db
        query = "INSERT INTO players (first_name, last_name, age, cap, pos, goals_scored, games_played, assists, team_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

        # run sql query
        cursor.execute(query, (player.fname, player.lname, player.age, player.cap,
                       player.pos, player.goals, player.games, player.assists, player.team_id))
        cnx.commit()

        # Print created players to terminal for debug and user feedback
        player_list.append(player.getAll())
        print(' Made player: {}'.format(vars(player)))

        # increments player position from list
        posCounter += 1

        # Reset Positions and increment team
        if(posCounter >= len(positions)):
            posCounter = 0
            team_id += 1
            i += 1


def randStaff(staffNumber=100):
    # THIS WILL EMPTY TABLE BEFORE SEEDING
    clear = "TRUNCATE TABLE `{}`.`team_staff`".format(DATABASE)
    cursor.execute(clear)

    print('Generating Staff')

    positions = ["Ticket Seller", "Janitor", "Water Person", "Physio", "Medic"]

    # init variables
    i = 0
    posCounter = 0
    team_id = 1

    while i < staffNumber:
        # Generate player
        staff = Staff(positions[posCounter], team_id)

        # create sql query to insert staff to db
        query = "INSERT INTO team_staff (first_name, last_name, job, team_id) VALUES (%s, %s, %s, %s)"

        # run sql query
        cursor.execute(query, (staff.fname, staff.lname,
                       staff.pos, staff.team_id))
        cnx.commit()

        # Print created staff to terminal for debug and user feedback
        staff_list.append(staff.getAll())
        print(' Made player: {}'.format(vars(staff)))

        # increments player position from list
        posCounter += 1

        # Reset Positions and increment team
        if(posCounter >= len(positions)):
            posCounter = 0
            team_id += 1
            i += 1


# Checks correct input if high number of operations
player_list = []
staff_list = []
if(pNum > 10):
    os.system('cls||clear')
    sanityCheck = input(
        '{} entities will be created. Are you sure? Type \'Y\' to continue or any other entry to escape. \n'.format(pNum * 11))

    if(sanityCheck.upper() == 'Y'):
        randPlayers()
        randStaff()
        cursor.close()
        cnx.close()
    else:
        print(sanityCheck)
        print('Aborting...')
        quit()
else:
    randPlayers()
    randStaff()
    cursor.close()
    cnx.close()
