# How to use this file
# Step 1: Create and click into the players table in phpmyadmin
# Step 2: Click import
# Step 3: Choose players.csv file in file browser
# Step 4: Change the "Lines Terminated" with option to a semicolon (;)
# Step 5: Paste the following column names into the "Column names" box: f_name,l_name,position,cap,age


import csv
import json
import random
import pyodbc


# import lists.py

# Lists for random assignment
firstNames = [
    "Adam", "Alex", "Aaron", "Ben", "Carl", "Dan", "David", "Edward", "Fred", "Frank", "George", "Hal", "Hank", "Ike", "John", "Jack", "Joe", "Larry", "Monte", "Matthew", "Mark", "Nathan", "Otto", "Paul", "Peter", "Roger", "Roger", "Steve", "Thomas", "Tim", "Ty", "Victor", "Walter"]

lastNames = [
    "Anderson", "Ashwoon", "Aikin", "Bateman", "Bongard", "Bowers", "Boyd", "Cannon", "Cast", "Deitz", "Dewalt", "Ebner", "Frick", "Hancock", "Haworth", "Hesch", "Hoffman", "Kassing", "Knutson", "Lawless", "Lawicki", "Mccord", "McCormack", "Miller", "Myers", "Nugent", "Ortiz", "Orwig", "Ory", "Paiser", "Pak", "Pettigrew", "Quinn", "Quizoz", "Ramachandran", "Resnick", "Sagar", "Schickowski", "Schiebel", "Sellon", "Severson", "Shaffer", "Solberg", "Soloman", "Sonderling", "Soukup", "Soulis", "Stahl", "Sweeney", "Tandy", "Trebil", "Trusela", "Trussel", "Turco", "Uddin", "Uflan", "Ulrich", "Upson", "Vader", "Vail", "Valente", "Van Zandt", "Vanderpoel", "Ventotla", "Vogal", "Wagle", "Wagner", "Wakefield", "Weinstein", "Weiss", "Woo", "Yang", "Yates", "Yocum", "Zeaser", "Zeller", "Ziegler", "Bauer", "Baxster", "Casal", "Cataldi", "Caswell", "Celedon", "Chambers", "Chapman", "Christensen", "Darnell", "Davidson", "Davis", "DeLorenzo", "Dinkins", "Doran", "Dugelman", "Dugan", "Duffman", "Eastman", "Ferro", "Ferry", "Fletcher", "Fietzer", "Hylan", "Hydinger", "Illingsworth", "Ingram", "Irwin", "Jagtap", "Jenson", "Johnson", "Johnsen", "Jones", "Jurgenson", "Kalleg", "Kaskel", "Keller", "Leisinger", "LePage", "Lewis", "Linde", "Lulloff", "Maki", "Martin", "McGinnis", "Mills", "Moody", "Moore", "Napier", "Nelson", "Norquist", "Nuttle", "Olson", "Ostrander", "Reamer", "Reardon", "Reyes", "Rice", "Ripka", "Roberts", "Rogers", "Root", "Sandstrom", "Sawyer", "Schlicht", "Schmitt", "Schwager", "Schutz", "Schuster", "Tapia", "Thompson", "Tiernan", "Tisler"
]

positions = ["Goalkeeper", "Right Back", "Left Back", "Center Back", "Sweeper",
             "Defensive Midfield", "Right Wing", "Center Midfield", "Striker", "Center Forward", "Left Wing"]


# Randomly selects from lists and combines
# 'playernumber' arg can be changed to alter the number of entries generated
def randPlayers(playerNumber=100):
    print('--- Generated Names ---')
    print(
        'fname' + ' ' +
        'lname' + ' ' +
        'position' + ' ' +
        'cap' + ' ' +
        'age')
    print('-----------------------')

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
        if(posCounter >= 11):
            posCounter = 0

    print('-----------------------')


# player
header = ["f_name", "l_name", "position", "cap", "age"]
player_list = []
# randPlayers(firstNames, lastNames)
randPlayers()


with open("players.csv", "w") as play:
    # Sets delimitation and line terminations for CSV file
    player = csv.writer(
        play,
        delimiter=",",
        quotechar='"',
        quoting=csv.QUOTE_ALL,
        lineterminator=';')

    # Writes player_list array to file
    player.writerows(player_list)
