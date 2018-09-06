# The total number of months included in the dataset
# The total net amount of "Profit/Losses" over the entire period
# The average change in "Profit/Losses" between months over the entire period
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period

import os
import csv

#  Lists to store data
# Lists to store data
date = []
profit = []


# Open the budget_data csv file
#budget_csv = os.path.join("budget_data.csv")

with open("budget_data.csv", newline="") as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=",")
    next (csvreader)   #  skip the first header row
    for row in csvreader:
        date.append(row[0])   #  get the dates into list
        profit.append(int(row[1])) #  get the profit into list 
        
#  calculate total profit


# print the output in terminal
print("Financial Analysis")
print("---------------------------------")
print("Total Month: " + str(len(profit)))
print("Total: $" + str(sum(profit)))
print("Greatest Increase in Profits: " + date[profit.index(max(profit))] + " ($" + str(max(profit)) + ")")



#  Open the output file and write to the file
output_file = os.path.join("budget_data_output.csv")

with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)
    # Write the header row
    writer.writerow(["Financial", "Analysis"])
    writer.writerow(["-------------------------------------------"]) 
    writer.writerow(["Total Month:" , str(len(profit))])
    writer.writerow(["Total:" , "$" + str(sum(profit))])
    writer.writerow(["Greatest Increase in Profits:", str(date[profit.index(max(profit))]), "($" + str(max(profit)) + ")"])
  







