import os
import csv

budget_csv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Resources', 'budget_data.csv')
totalAmt = int(0)
totalMths = []
priorMth = int(0)
maxDeltaAmt = int(0)
minDeltaAmt = int(0)
totalDelta = []

with open(budget_csv_path, newline='') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')
	csv_header = next(csvreader)
    
	for row in csvreader:
		totalAmt = int(row[1]) + totalAmt
		totalMths.append(row[0])
		
		if priorMth != 0:
			delta= int(row[1]) - int(priorMth)
			priorMth = row[1]
			totalDelta.append(delta)
		else:
			delta = int(0)
			priorMth = int(row[1])
		
		if delta > maxDeltaAmt:
			maxDeltaAmt = delta
			year, month = row[0].split("-")
			year = ("20") + year 
			maxDeltaMth = '-'.join((month, year))
		
		if delta < minDeltaAmt:
			minDeltaAmt = delta
			year, month = row[0].split("-")
			year = ("20") + year 
			minDeltaMth = '-'.join((month, year))
			
avgDelta = round(sum(totalDelta) / len(totalDelta), 2)

print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(len(set(totalMths))))
print("Total: $" + str(totalAmt))
print("Average Change: $" + str(avgDelta))
print("Greatest Increase in Profits: " + maxDeltaMth + " ($" + str(maxDeltaAmt) + ")")
print("Greatest Decrease in Profits: " + minDeltaMth + " ($" + str(minDeltaAmt) + ")")

outputFile = open("output.txt", "w+")
outputFile.write("Financial Analysis" + '\n')
outputFile.write("----------------------------" + '\n')
outputFile.write("Total Months: " + str(len(set(totalMths))) + '\n')
outputFile.write("Total: $" + str(totalAmt) + '\n')
outputFile.write("Average Change: $" + str(avgDelta) + '\n')
outputFile.write("Greatest Increase in Profits: " + maxDeltaMth + " ($" + str(maxDeltaAmt) + ")" + '\n')
outputFile.write("Greatest Decrease in Profits: " + minDeltaMth + " ($" + str(minDeltaAmt) + ")" + '\n')
outputFile.close()