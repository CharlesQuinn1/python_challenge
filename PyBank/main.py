import os
import csv
import pandas as pd

# Change directory to current working directory of main.py file
dirname = os.path.dirname(__file__)
dirname = dirname + chr(92)
os.chdir(dirname)

date_v = []
profit_loss_v = []

# Change directory to point to data file
budget_data_csv = os.path.join("Resources","budget_data.csv")

with open(budget_data_csv,'r') as csvfile:
    budget_file = csv.DictReader(csvfile,delimiter=',')
    mnth_ttl = 0
    pl_ttl = 0
    i = 0
    chng_prof = dict()
    for row in budget_file:
        # print(row["Date"],row["Profit/Losses"])
        if len(row["Date"]) > 0:
            mnth_ttl = mnth_ttl + 1
        pl_ttl = pl_ttl + int(row["Profit/Losses"])
    print(f"Total Months: {mnth_ttl}")
    print(f"Total: {pl_ttl}")
    print(f"average: {pl_ttl/mnth_ttl}")
df = pd.DataFrame(budget_file)
df