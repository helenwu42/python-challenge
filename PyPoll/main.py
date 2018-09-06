#  The total number of votes cast
#  A complete list of candidates who received votes
#  The percentage of votes each candidate won
#  The total number of votes each candidate won
#  The winner of the election based on popular vote

import os
import csv

# Lists to store data
vote = []                  # the voter id
candidate = []             # the candidicates votes
uniqueC = []               # The unique candicates


# Open the election_data csv file

with open("election_data.csv", newline="") as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=",")
    next (csvreader)   #  skip the first header row
    for row in csvreader:
        vote.append(row[0])        #  get the vote id in the list
        candidate.append(row[2])   #  get the candidate in the list
    
    for x in candidate:
        if x not in uniqueC:
            uniqueC.append(x)
    


# print the output in terminal
print("Election Results")
print("---------------------------------")
print("Total Votes: " + str(len(vote)))
print("---------------------------------")



