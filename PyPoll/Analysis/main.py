import os
import csv

election_data = os.path.join('..', 'Resources', 'election_data.csv')

#defining variables
total_votes = 0
C_C_S = "Charles Casper Stockham"
Stockham_votes = 0
D_D = "Diana DeGette"
DeGette_votes = 0
R_A_D = "Raymon Anthony Doane"
Doane_votes = 0

with open(election_data, 'r') as csvfile: #opening csv file to read the data
    csv_reader = csv.reader(csvfile)

    header = next(csv_reader) #skipping data in header row and storing as a variable

    for row in csv_reader:
        #calculate total voters
        total_votes += 1
        #calculate votes for the candidates
        if row[2] == C_C_S:
            Stockham_votes += 1
        elif row[2] == D_D:
            DeGette_votes += 1
        elif row[2] == R_A_D:
            Doane_votes += 1
    
    #calculate percentages after loop has stopped counting
    Stockham_percent = (Stockham_votes / total_votes) * 100
    DeGette_percent = (DeGette_votes / total_votes) * 100
    Doane_percent = (Doane_votes / total_votes) * 100
    
    #make a dictionary of the variables
    candidate_list = {
        (Stockham_percent): C_C_S,
        (DeGette_percent): D_D,
        (Doane_percent): R_A_D
    }
    #create a variable that locates the winner
    winner = (candidate_list.get(max(candidate_list)))
    
output = (f"""
Election Results
------------------------------
Total Votes: {total_votes}
-------------------------------
Charles Casper Stockham: {Stockham_percent:.3f}% ({Stockham_votes}) 
Diana DeGette: {DeGette_percent:.3f}% ({DeGette_votes})
Raymon Anthony Doane: {Doane_percent:.3f}% ({Doane_votes})
-------------------------------
Winner: {winner}
-------------------------------
""")
#----------------------------------------------------------------------------------
file = os.path.join('..', 'Analysis', 'text_output.txt')
with open(file, 'w') as textfile:
    textfile.write(output)