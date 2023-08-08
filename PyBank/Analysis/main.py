import os
import csv

budget_csv = os.path.join('..', 'Resources', 'budget_data.csv')

months_list = []
total = 0

#total_profit_loss = 0
#change = []
#number_rows = 0
greatest_increase = 0
greatest_increase_month = ""
greateat_decrease = 0
greatest_decrease_month = ""

with open(budget_csv, 'r') as csvfile:
    csv_reader = csv.reader(csvfile)

    header = next(csv_reader)
    prev_value_i = False
    prev_value_d = False

    for row in csv_reader:
        total += int(row[1])
        month = row[0]
        if month not in months_list:
            months_list.append(month)
        
        #profit_losses = int(row[1])
        #number_rows += 1
        #total_profit_loss += profit_losses

        current_value = int(row[1])

        if prev_value_i is not False:
            change_i = current_value - prev_value_i
            if change_i > greatest_increase:
                greatest_increase = change_i
                greatest_increase_month = month
        prev_value_i = current_value

        if prev_value_d is not False:
            change_d = current_value - prev_value_d
            if change_d < greateat_decrease:
                greateat_decrease = change_d
                greatest_decrease_month = month
        prev_value_d = current_value

print("Financial Analysis")
print("------------------------------")

month_count = len(months_list)
print("Total Months:", month_count)

print("Total: $" + str(total))

#average_change = (total_profit_loss / month_count)
#print("Average Change: " + str(average_change))
print("Greatest Increase in Profits:", greatest_increase_month, "($" + str(greatest_increase) + ")")

print("Greatest Decrease in Profits:", greatest_decrease_month, "($" + str(greateat_decrease) + ")")