import os
import csv
import datetime

# Change directory to current working directory of main.py file
dirname = os.path.dirname(__file__)
dirname = dirname + chr(92)
os.chdir(dirname)

date_v = []
profit_loss_v = []

# Change directory to point to data file
budget_data_csv = os.path.join("Resources","budget_data.csv")

with open(budget_data_csv,'r') as csvfile:
    bud_file = csv.Reader(csvfile,delimiter=',')
    # print(list(bud_file))
    for line in bud_file:
        print("Date",csvreader["Profit/Losses"][line])

