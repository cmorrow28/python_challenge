import os
import csv

budget_csv = os.path.join('..', 'Resources', 'budget_data.csv')

#defining my variables
total_months = 0
total_profit = 0
total_change = 0
max_value = 0
max_month = ("")
lowest_value = 0
lowest_month = ("")

with open(budget_csv, 'r') as csvfile: #opening the csv file to read the data
    csv_reader = csv.reader(csvfile)

    header = next(csv_reader) #skipping data in header row and storing it as a variable
    first_row = next(csv_reader) #skipping first row of data and storing as a variable (for change calculation)

    previous_value = int(first_row[1]) #defining previous_value as the first row of coloumn 2

    for row in csv_reader: #read through the data in the csv file row by row
       #calculate total months
        total_months += 1
        total_profit += previous_value
       #calculate total profits
        changes = int(row[1]) - previous_value
        previous_value = int(row[1])
        total_change += changes
       #calculate greatest increase value
        if changes > max_value:
            max_value = changes
            max_month = row[0]
        #calculate greatest decrease value
        if changes < lowest_value:
            lowest_value = changes
            lowest_month = row[0]      
#---------------------------------------------------------------------------------
output = f"""
Financial Analysis
------------------------------
Total Months: {total_months + 1}
Total: ${total_profit + int(row[1])}
Average Change: ${(total_change / total_months):.2f}
Greatest Increase in Profits: max_month ${max_value}
Greatest Increase in Profits: lowest_month ${lowest_value}
"""
#----------------------------------------------------------------------------------
file = os.path.join('..', 'Analysis', 'text_output.txt')
with open(file, 'w') as textfile:
    textfile.write(output)