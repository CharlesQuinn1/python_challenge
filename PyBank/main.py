import os
import csv


# Change directory to current working directory of main.py file at
# \Bootcamp\Homework\python_challenge\PyBank\main.py
# then change directory to point to Resources folder
dirname = os.path.dirname(__file__)
dirname = dirname + chr(92)
os.chdir(dirname)
budget_data_csv = os.path.join("Resources","budget_data.csv")

# Create blank dictionary to hold monthly profit/loss change
mnth_chng = {'Date':[],'Chng':[]}


with open(budget_data_csv,'r') as csvfile:
    budget_file = csv.DictReader(csvfile,delimiter=',')
    mnth_ttl = 0
    pl_ttl = 0
    i = 0
    sum_pl = 0
    for row in budget_file:

# Calculate profit/loss grand total (mnth_ttl)
        if len(row["Date"]) > 0:
            mnth_ttl = mnth_ttl + 1
        pl_ttl = pl_ttl + int(row["Profit/Losses"])

# Calculate monthly profit/loss change and append to empty dictionary (mnth_chng)
        if i == 0:
            prev_mnth = row["Date"]
            prev_pl = int(row["Profit/Losses"])
            i = i + 1
        else:
            cur_mnth = row["Date"]
            cur_pl = int(row["Profit/Losses"])
            pl_chng = cur_pl - prev_pl
            prev_pl = cur_pl
            mnth_chng['Date'].append(cur_mnth)
            mnth_chng['Chng'].append(pl_chng)
            sum_pl = sum_pl + pl_chng
            i = i + 1

# Reading from mnth_chng dictionary Calculate Min/Max profit/loss change
# and the month associated with those amounts
    max_value = round(float(max(list(mnth_chng["Chng"]))),0)
    min_value = round(float(min(list(mnth_chng["Chng"]))),0)
    p = 0
    for line in mnth_chng["Chng"]:
        amt = round(float(mnth_chng["Chng"][p]),0)
        if amt == max_value:
            dt_mx = mnth_chng["Date"][p]
            avg_mx = mnth_chng["Chng"][p]
        if amt == min_value:
            dt_mn = mnth_chng["Date"][p]
            avg_mn = mnth_chng["Chng"][p]
        p = p + 1
    avg_chng = round(sum_pl/len(mnth_chng['Chng']),2)

# Print analysis to the terminal
    print(" ")
    print("Financial Analysis")
    print(" ")
    print("-----------------------------------")
    print(" ")
    print(f"Total Months: {mnth_ttl}")
    print(" ")
    print(f"Total: ${pl_ttl}")
    print(" ")
    print(f"Average Change: ${avg_chng}")
    print(" ")
    print(f"Greatest Increase in Profits: {dt_mx} (${avg_mx})")
    print(" ")
    print(f"Greatest Decrease in Profits: {dt_mn} (${avg_mn})")
    print(" ")

# Write analysis to file
# Specify the file to write to
dirname = os.path.dirname(__file__)
dirname = dirname + chr(92)
os.chdir(dirname)
output_path = os.path.join("analysis", "analysis.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(['Financial Analysis', '', ''])
    csvwriter.writerow(['-----------------------------------', '', ''])
    csvwriter.writerow(['Total Months: ',mnth_ttl,''])
    csvwriter.writerow(['Total: $',pl_ttl,''])
    csvwriter.writerow(['Average Change: $',avg_chng,''])
    csvwriter.writerow(['Greatest Increase in Profits: ',dt_mx, avg_mx])
    csvwriter.writerow(['Greatest Decrease in Profits: ',dt_mn, avg_mn])