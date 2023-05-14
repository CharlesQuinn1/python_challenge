import os
import csv


# Change directory to current working directory of main.py file at
# \Bootcamp\Homework\python_challenge\PyBank\main.py
# then change directory to point to Resources folder
dirname = os.path.dirname(__file__)
dirname = dirname + chr(92)
os.chdir(dirname)
election_data_csv = os.path.join("Resources","election_data_test.csv")

# Create blank dictionary to hold monthly profit/loss change
elect_dict = {'Ballot ID':[],'County':[],'Candidate':[]}
vote_count = {'Candidate':[],'Vote':[]}

with open(election_data_csv,'r') as csvfile:
    election_file = csv.DictReader(csvfile,delimiter=',')

    j = 0

    for row in election_file:
        elect_dict['Ballot ID'].append(row['Ballot ID'])
        elect_dict['County'].append(row['County'])
        elect_dict['Candidate'].append(row['Candidate'])
        j = j + 1
    i = 0
    can_prev = ''
    can_cur = elect_dict['Candidate'][i]

    k = 0

    for row in elect_dict:
        k = k + 1
        if i == 0:
            can_cur = elect_dict['Candidate'][i]
            i = i + 1
        else:
            can_prev = can_cur
            can_cur = elect_dict['Candidate'][i]
            if can_prev != can_cur:
                vote_count['Candidate'].append(row[can_prev])
                vote_count['Vote'].append(i)
                i = i + 1
            else:
                i = i + 1
print('j: ',j)
print('k: ',k)
print('i: ',i)

        # i = 0
        # ballot_ttl = 0
        # ballot_grnd_ttl = 0
        # test = 0
        # can_cur = ''
        # can_prev = ''
        # o = 0
        # for row in elect_dict:
        #     o = o + 1
        #     if i == 0:
        #         can_cur = elect_dict['Candidate'][i]
        #         i = i + 1
        #     else:
        #         if can_prev != can_cur:
        #             vote_count['Candidate'].append(can_prev)
        #             vote_count['Vote'].append(i)
        #             ballot_ttl = i
        #             can_cur = elect_dict['Candidate'][i]
        #             can_prev = can_cur
        #             i = i + 1
        #         else:
        #             can_cur = elect_dict['Candidate'][i]
        #             can_prev = can_cur
        #             i = i + 1

        #     print('can_cur: ',can_cur)
        #     print('can_prev: ',can_prev)
        #     print('O: ',o)
        #     print(vote_count)
        # print('j: ',j)
