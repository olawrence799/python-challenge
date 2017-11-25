import os
import csv
import operator
import sys
from collections import Counter

vote_counter = -1 #set to -1 to account for the header
candidates = []
voted_candidates = []
cnt = Counter()

election_csv_path = os.path.join("..","PyPoll", "election_data_1.csv")

#sys.stdout = open('election_results.txt', 'w') #to write directly to file, no printing to the terminal

def fprint(output):
    print(output)
    with open('election_results.txt', 'a') as f:
        f.write("{}\n".format(output))

with open(election_csv_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    for row in csvreader:
        if len(row[0]) > 0:
            vote_counter = vote_counter + 1
            candidate = (row[2]) #takes the candidate name voted for in the row, along with the header
            voted_candidates.append(candidate)

    for candidate in voted_candidates:
        cnt[candidate] += 1
        if candidate not in candidates:
            candidates.append(candidate)
    
    del candidates[0]

    fprint("Election Results")
    fprint("-------------------------")
    fprint("Total Votes: " + str(vote_counter)) #returns the total number of votes
    fprint("-------------------------")

    for key in cnt:
        if key in candidates:
            percent_votes = cnt[key]/vote_counter
            fprint(key + ": " + str(100*percent_votes) + "%" + " (" + str(cnt[key]) + ")") #cnt[key] returns the value for that key in the 'cnt' dictionary

    fprint("-------------------------")
    fprint("Winner: " + max(cnt.items(), key=operator.itemgetter(1))[0])
    fprint("-------------------------")

#sys.stdout.close()