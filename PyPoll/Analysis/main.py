import os
import csv

election_data = os.path.join('..', 'Resources', 'election_data.csv')

voters_list = []
voter_id = 0

with open(election_data, 'r') as csvfile:
    csv_reader = csv.reader(csvfile)

    header = next(csv_reader)

    for row in csv_reader:
        voter_id += int(row[0])
        voters = row[0] 
        if voters not in voters_list:
            voters_list.append(voters)

total_voters = len(voters_list)
print("Total Votes: " + str(total_voters))


