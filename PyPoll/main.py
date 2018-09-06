#  The total number of votes cast
#  A complete list of candidates who received votes
#  The percentage of votes each candidate won
#  The total number of votes each candidate won
#  The winner of the election based on popular vote

import os
import csv
from collections import Counter

# Lists to store data
vote = []                  # the voter id
candidate = []             # the candidicates votes
uniqueC = {}               #  the dictionary holdd the unique candidate and number of votes
key = []                   #  The unqie candicate in a list
value = []                 #  The number of votes for each candidate in a list
percentage = []            #  The percentage of votes for each candidate in a list

# Open the election_data csv file

with open("election_data.csv", newline="") as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=",")
    next (csvreader)   #  skip the first header row
    for row in csvreader:
        vote.append(row[0])        #  get the vote id in the list
        candidate.append(row[2])   #  get the candidate in the list
    

    #  store the unique candidate and number of votes in a dictionary
    uniqueC = Counter(candidate)
    
    #  store unique candicate in a list
    for i in uniqueC.keys():
        key.append(i)
    
    # Store unique votes for each candiates in a list
    for i in uniqueC.values():
        value.append(i)

    # Store the percenatge of votes each candicate has in a list
    for x in range(len(value)):
        percentage.append(round(((value[x]/sum(value))*100), 3))

 
# print the output in terminal
print("Election Results")
print("---------------------------------")
print("Total Votes: " + str(len(vote)))
print("---------------------------------")
for i in range(0, 4):
    print(str(key[i]) + ":   " + str(percentage[i]) + "%   " + "(" + str(value[i]) + ")")
print("---------------------------------")
print("Winner:  " + max(uniqueC, key=uniqueC.get))
print("---------------------------------")

#  Open the output file and write to the file
output_file = os.path.join("election_data_output.csv")

with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # writer.writerow(["Total Month:" , str(len(profit))])
    writer.writerow(["Election", "Results"])
    writer.writerow(["---------------------------------"])
    writer.writerow(["Total Votes: " , str(len(vote))])
    writer.writerow(["---------------------------------"])
    for i in range(0, 4):
        writer.writerow([str(key[i]) + ":" , str(percentage[i]) + "%" ,  str(value[i])])
    writer.writerow(["---------------------------------"])
    writer.writerow(["Winner:  " , max(uniqueC, key=uniqueC.get)])
    writer.writerow(["---------------------------------"])

