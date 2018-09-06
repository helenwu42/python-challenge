# The total number of months included in the dataset
# The total net amount of "Profit/Losses" over the entire period
# The average change in "Profit/Losses" between months over the entire period
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period

import os
import csv

# Lists to store data
date = []                  # the date of the profit/loss
profit = []                # the amount of profit/loss
diff = []                  # the difference of profit/loss


# Open the budget_data csv file


with open("budget_data.csv", newline="") as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=",")
    next (csvreader)   #  skip the first header row
    for row in csvreader:
        date.append(row[0])   #  get the dates into list
        profit.append(int(row[1])) #  get the profit into list 
        
#  diff list
for x in range(0, len(profit)):
    diff.append(int(profit[x])-int(profit[x-1]))
diff.pop(0)


# print the output in terminal
print("Financial Analysis")
print("---------------------------------")
print("Total Month: " + str(len(profit)))
print("Total: $" + str(sum(profit)))
print("Average Change: " + "$" + str(round(sum(diff)/(len(profit)-1), 2)))
print("Greatest Increase in Profits: " + date[profit.index(max(profit))] + " ($" + str(max(profit)) + ")")
print("Greatest Decrease in Profits: " + date[profit.index(min(profit))] + " ($" + str(min(profit)) + ")")



#  Open the output file and write to the file
output_file = os.path.join("budget_data_output.csv")

with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)
    # Write the header row
    writer.writerow(["Financial", "Analysis"])
    writer.writerow(["-------------------------------------------"]) 
    writer.writerow(["Total Month:" , str(len(profit))])
    writer.writerow(["Total:" , "$" + str(sum(profit))])
    writer.writerow(["Average Change: " , "$" + str(round(sum(diff)/(len(profit)-1), 2))])
    writer.writerow(["Greatest Increase in Profits:", str(date[profit.index(max(profit))]), "($" + str(max(profit)) + ")"])
    writer.writerow(["Greatest Decrease in Profits:", str(date[profit.index(min(profit))]), "($" + str(min(profit)) + ")"])
  







