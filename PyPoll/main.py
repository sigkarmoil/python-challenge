import os
import csv
import statistics
import itertools

poll_voters= []
poll_candidate = []

#1. opening the file
#Remember to fix the csv path later
#csvpath= os.path.join('Resources','budget_data.csv')
csvpath= (r'C:\Users\haeze\OneDrive\Documents\GitHub\python-challenge\PyPoll\Resources\election_data.csv')
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #object type
    
    csv_header = next(csvreader)
    
    for rows in csvreader:
        poll_voters.append(rows[0])
        poll_candidate.append(rows[2])

total_votes = len(poll_voters)


#2. Printing the candidates
#2.1 finding unique candidate name
candidate_name = []
for person in poll_candidate:
    if person not in candidate_name:
        candidate_name.append(person)


#2.2 totalling candidate vote at each_cand_votes
##create receptacle to store candidate votes. This receptacle will automatically change if new candidates join, or if candidate decrease
each_cand_votes= list(itertools.repeat(0,len(candidate_name) ) )

#2.3 add unique candidates
##automatically add number of votes, based on matching name.
for x in poll_candidate:
    each_cand_votes[candidate_name.index(x)]=each_cand_votes[candidate_name.index(x)]+1

#2.4 For Loop to print the candidates performances
def myformat(x):
    return ('%.2f' % x).rstrip('0').rstrip('.')
csv_output=(r"C:\Users\haeze\OneDrive\Documents\GitHub\python-challenge\PyPoll\analysis\analysis.csv")
with open(csv_output,'w') as csv_writer:
    csv_writer = csv.writer(csv_writer, delimiter=',')
    csv_writer.writerow([ f"Election Results" ])
    csv_writer.writerow([ f"----------------------------------- " ])
    csv_writer.writerow([ f" Total Votes: {total_votes} " ])  
    for x in range(len(candidate_name)):
        csv_writer.writerow( [f"{candidate_name[x]}: { myformat( (each_cand_votes[x]/total_votes)*100 ) }% ({each_cand_votes[x]})"])
    csv_writer.writerow([ f"Winner: {candidate_name[ each_cand_votes.index( max(each_cand_votes) ) ] } " ])
