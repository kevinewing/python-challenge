#PyBank/main.py
import os
import csv


months = 0
profit = 0
change_list = []
previousValue = 0
maxamt = 0
minamt = 0

csvpath = os.path.join("Resources", "budget_data.csv")

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    profit
    for row in csvreader:
        months += 1
        profit = profit + float(row[1])
        if float(row[1]) > maxamt:
            maxamt = float(row[1]) 
            maxdate = row[0]
        if float(row[1]) < minamt:
            minamt = float(row[1])
            mindate = row[0]
        

average = profit / months

print("Financial Analysis")
print("----------------------------")

print("Total Months: " + str(months))
print("Total: $" + str(format(profit,".2f")))
print("Average Change: $" + str(format(average,".2f")))
print("Greatest Increase in Profits: " + maxdate + " (" + str(format(maxamt,".2f")) + ")")
print("Greatest Decrease in Profits: " + mindate + " (" + str(format(minamt,".2f")) + ")")  

output_path = os.path.join("output.csv")
with open(output_path,'w' , newline='') as csvoutputfile:
    csvwriter = csv.writer(csvoutputfile, delimiter=',')
    csvwriter.writerow(["Total Months:", months])
    csvwriter.writerow(["Total:", format(profit,".2f")])
    csvwriter.writerow(["Greatest Increase in Profits:", maxdate, format(maxamt,".2f")])
    csvwriter.writerow(["Greatest Decrease in Profits:", mindate, format(minamt,".2f")])