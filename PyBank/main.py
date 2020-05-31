import os
import csv
import statistics

fin_data_month= []
fin_data_money= []

#opening the file
#Remember to fix the csv path later
csvpath= os.path.join('Resources','budget_data.csv')
#csvpath= (r'C:\Users\haeze\OneDrive\Documents\GitHub\python-challenge\PyBank\Resources\budget_data.csv')
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #object type
    
    csv_header = next(csvreader)
    
    for rows in csvreader:
        fin_data_month.append(rows[0])
        fin_data_money.append(int(rows[1]) )


money_sum = 0
for entries in fin_data_money:
    money_sum = money_sum + entries

#calculating changes in profit
delta_money_cal=0
delta_money = []
for j in range(len(fin_data_money)-1 ):
    delta_money_cal= fin_data_money[j+1] - fin_data_money[j]
    delta_money.append(delta_money_cal)

#Code to adjust decimal number in float
mean_delta_money= statistics.mean(delta_money)

#print out to csv

#csv_output=(r"C:\Users\haeze\OneDrive\Documents\GitHub\python-challenge\PyBank\analysis\analysis.csv")
csv_output=os.path.join("analysis","analysis.csv")
with open(csv_output,'w', newline='') as csv_writer:
    csv_writer = csv.writer(csv_writer, delimiter=',')
    csv_writer.writerow(['Financial Analysis'])
    csv_writer.writerow(["---------------------------------"])
    csv_writer.writerow([f"Total Months: {len(fin_data_month)}"])
    csv_writer.writerow([f"Total: ${money_sum}"] )
    csv_writer.writerow([f"Average Change: ${round(mean_delta_money, 4) }"])
    csv_writer.writerow([f"Greatest Increase in Profits: ${max(delta_money)} "])
    csv_writer.writerow([f"Smallest Decrease in Profits: ${min(delta_money)} "])
