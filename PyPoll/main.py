import os
import csv
from collections import OrderedDict
import pandas as pd
from pathlib import Path

# Change directory to current working directory of main.py file at
# \Bootcamp\Homework\python_challenge\PyBank\main.py
# # then change directory to point to Resources folder
dirname = os.path.dirname(__file__)
dirname = dirname + chr(92)
os.chdir(dirname)
election_data_csv = os.path.join("Resources", "election_data.csv")

# Read Election Data file
df = pd.read_csv(election_data_csv)

# Calculate votes
df_grp = df.groupby(['Candidate']).count()
df_grp['vote_ttl'] = df_grp['Ballot ID'].sum()
df_grp['vote_pct'] = df_grp['Ballot ID'] / df_grp['vote_ttl']
df_grp['vote_pct'] = (df_grp['vote_pct']*100).map("{:.3f}%".format)
df_reset = df_grp.reset_index()

# Calculate winner
win_ttl = df_reset['Ballot ID'].max()
win = df_reset['Candidate'].loc[df_reset['Ballot ID'] == win_ttl]

# Print Results
print(' ')
print('Election Results')
print('-'*100)
print(' ')
print('Total Votes: ',df_reset['vote_ttl'][0])
print(' ')
print('-'*100)
print(' ')
print(df_reset['Candidate'][0],": ",df_reset['vote_pct'][0]," (",df_reset['Ballot ID'][0],")")
print(' ')
print(df_reset['Candidate'][1],": ",df_reset['vote_pct'][1]," (",df_reset['Ballot ID'][1],")")
print(' ')
print(df_reset['Candidate'][2],": ",df_reset['vote_pct'][2]," (",df_reset['Ballot ID'][2],")")
print(' ')
print('-'*100)
print(' ')
print('Winner: ',win.iloc[0])
print(' ')
print('-'*100)

# format final output
df_reset['votes'] = df_reset['Ballot ID']
df_reset['Winner'] = win.iloc[0]

# Write Results to a file
election_results = os.path.join("analysis", "election_results.csv")
df_reset.to_csv(election_results, index=False, columns=['Candidate','votes','vote_pct','Winner'])