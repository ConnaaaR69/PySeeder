# How to use this file
# Step 1: Create and click into the players table in phpmyadmin
# Step 2: Click import
# Step 3: Choose players.csv file in file browser
# Step 4: Change the "Lines Terminated" with option to a semicolon (;)
# Step 5: Paste the following column names into the "Column names" box: f_name,l_name,position,cap,age

import csv
import json
import random


# Randomly selects from lists and combines
# 'playernumber' arg can be changed to alter the number of entries generated
def randPlayers(playerNumber=22):
    print('--- Generated Player Names ---')
    print(
        'fname' + ' ' +
        'lname' + ' ' +
        'position' + ' ' +
        'cap' + ' ' +
        'age')
    print('-----------------------')
    positions = ["Goalkeeper", "Right Back", "Left Back", "Center Back", "Sweeper",
                 "Defensive Midfield", "Right Wing", "Center Midfield", "Striker", "Center Forward", "Left Wing"]
    i = 0
    posCounter = 0
    while i < playerNumber:
        # id = i + 1

        file = open('names.json')
        data = json.load(file)
        fname = random.choice(data['names'])
        lname = random.choice(data['names'])
        position = positions[posCounter]
        cap = random.randint(1, 50)
        age = random.randint(18, 31)

        temp = [
            fname,
            lname,
            position,
            cap,
            age]
        player_list.append(temp)
        # output generated names
        print(
            fname + ' ' +
            lname + ' ' +
            position + ' ' +
            str(cap) + ' ' +
            str(age))

        # iterate
        i += 1
        posCounter += 1
        if(posCounter >= len(positions)):
            posCounter = 0

    print('-----------------------')


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
randPlayers()
randStaff()
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
