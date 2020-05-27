import pandas as pd
poll=pd.read_csv(r'C:\Users\haeze\OneDrive\Documents\GitHub\python-challenge\PyPoll\Resources\election_data.csv')

total_vote=poll["Candidate"].count()
poll_count= poll["Candidate"].value_counts()
poll_perc = poll["Candidate"].value_counts(normalize = True)

poll_combine= pd.concat([poll_count, poll_perc], axis= 1)
#renaming column
poll_combine.columns.values[[0,1]] = ['Total Votes',' Percentage']

winner = poll_perc.index[0]

print(f"Total Votes : {total_vote}")
print( poll_combine)
print(f"The winner is: {winner}")
#print(poll_count.head() )
#print(poll_perc.head() )