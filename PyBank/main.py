# The total number of months included in the dataset
# The total net amount of "Profit/Losses" over the entire period
# The average change in "Profit/Losses" between months over the entire period
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period

import os
import csv

#  Lists to store data
totalMonth = 0             #  number of months
totalNet = 0               #  The total net amount of "Profit/Losses" over the entire period
greatestIncreaseM = ""     #  keep track of the greatest increase month
greatestDecreaseM = ""     #  keep track of the greatest decrease month
greatestIncrease = 0       #  keep track of the greatest increase amount 
greatestDecrease = 0       #  keep track of the greatest decrease amount



# Open the budget_data csv file
budget_csv = os.path.join("budget_data.csv")

with open(budget_csv, newline="") as csvfile:
    next (csvfile)   #  skip the first header row
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        totalMonth = totalMonth + 1                # Track total month
        totalNet = totalNet + int(row[1])          # Track total net amount
        if greatestIncrease < int(row[1]):
            greatestIncrease = int(row[1])
            greatestIncreaseM = row[0]
        if greatestDecrease > int(row[1]):
            greatestDecrease = int(row[1])
            greatestDecreaseM = row[0]             
         
        

# print the output in terminal
print("Financial Analysis")
print("---------------------------------")
print("Total Month: " + str(totalMonth))
print("Total: $" + str(totalNet))
print("Greatest Increase in Profit: " + greatestIncreaseM + " " + "($" + str(greatestIncrease) + ")")
print("Greatest Decrease in Profit: " + greatestDecreaseM + " " + "($" + str(greatestDecrease) + ")")


#  Open the output file and write to the file
output_file = os.path.join("budget_data_output.csv")

with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)
    # Write the header row
    writer.writerow(["Financial", "Analysis"])
    writer.writerow(["-------------------------------------------"]) 
    writer.writerow(["Total Month:" , str(totalMonth)])
    writer.writerow(["Total:" , "$" + str(totalNet)])
    writer.writerow(["Greatest Increase in Profits: ", greatestIncreaseM, "($" + str(greatestIncrease) + ")"])
    writer.writerow(["Greatest Decrease in Profits: ", greatestDecreaseM, "($" + str(greatestDecrease) + ")"])







