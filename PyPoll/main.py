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

# Open the election_data csv file

with open("election_data.csv", newline="") as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=",")
    next (csvreader)   #  skip the first header row
    for row in csvreader:
        vote.append(row[0])        #  get the vote id in the list
        candidate.append(row[2])   #  get the candidate in the list
    

    #  store the unique candidate and number of votes in a dictionary
    uniqueC = Counter(candidate)
    
    for i in uniqueC.keys():
        key.append(i)
    
    for i in uniqueC.values():
        value.append(i)

    # find number of votes and store in a dictionary
   
    

    #  find the winnervotes
    winnervotes= max(value)
    print(winnervotes)
    
    

    
        
    
# print the output in terminal
print("Election Results")
print("---------------------------------")
print("Total Votes: " + str(len(vote)))
print("---------------------------------")



