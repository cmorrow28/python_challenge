import os
import csv

budget_csv = os.path.join('..', 'Resources', 'budget_data.csv')

months_list = []

with open(budget_csv, 'r') as csvfile:
    csv_reader = csv.reader(csvfile)

    header = next(csv_reader)

    total = 0
    for row in csv_reader:
        total += int(row[1])
        month = row[0]
        if month not in months_list:
            months_list.append(month)

month_count = len(months_list)

print("Financial Analysis")
print("------------------------------------")
print("Total Months:", month_count)
print("Total: $" + str(total))

