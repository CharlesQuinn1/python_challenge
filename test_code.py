import os
import csv
from collections import OrderedDict
import pandas as pd


# Change directory to current working directory of main.py file at
# \Bootcamp\Homework\python_challenge\PyBank\main.py
# then change directory to point to Resources folder
dirname = os.path.dirname(__file__)
dirname = dirname + chr(92)
os.chdir(dirname)
election_data_csv = os.path.join("PyPoll", "Resources", "election_data_test.csv")

# print(dirname)
# print(election_data_csv)

# Create blank dictionary to hold monthly profit/loss change
elect_dict = {'Ballot ID','County','Candidate'}
vote_count = {'course':300}

with open(election_data_csv,'r',newline='') as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=',')
    
    for x in csvreader:
        bal = x['Ballot ID']
        cou = x['County']
        can = x['Candidate']
        print('Bal: ', bal,' cou:',cou,' can:',can)
        # var = '"' + bal + ',' + cou + ',' + can + '"'
        # elect_dict.update(var)
    i = 0
    j = 0
    name1 = ''
    name2 = ''
    # for row in csvreader:
    #     if i == 0:
    #         name1 = row['Candidate']
    #         name2 = row['Candidate']
    #         i = i + 1
    #     else:
    #         if name1 != name2:
    #             j = 0
    #         j = j + 1
    #         name1 = name2
    #         name2 = row['Candidate']
    #         i = i +1
    #     print('i: ',i,' j: ',j, 'name1: ',name1,' name2: ',name2)            
#        print(vote_count)
# print(elect_dict)
# print(bal,cou,can)

    
