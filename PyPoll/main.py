import os
import csv


# Change directory to current working directory of main.py file at
# \Bootcamp\Homework\python_challenge\PyBank\main.py
# then change directory to point to Resources folder
dirname = os.path.dirname(__file__)
dirname = dirname + chr(92)
os.chdir(dirname)
election_data_csv = os.path.join("Resources","election_data.csv")

with open(election_data_csv,'r') as csvfile:
    budget_file = csv.DictReader(csvfile,delimiter=',')