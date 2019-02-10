import os
import csv

poll_csv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Resources', 'election_data.csv')
totalAmt = int(0)
amtCheck = int(0)
candidatesList = []
candidateUnique = []
candidateCount = []
candidatePerc = []
txtOutput = str('-------------------------' + '\n')

with open(poll_csv_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        totalAmt = totalAmt + 1
        candidatesList.append(row[2])

candidateUnique = set(candidatesList)

for row in candidateUnique:
    candidateCount.append(candidatesList.count(row))

for row in candidateCount:
    candidatePerc.append(round(((row / totalAmt)*100), 3))

completeList = sorted(zip(candidateUnique, candidatePerc, candidateCount), key=lambda x: x[1], reverse=True)

print('Election Results')
print('-------------------------')
print('Total Votes: ' + str(totalAmt))
print('-------------------------')
for x, y, z in completeList:
    print(str(x) + ': ' + str(y) + '% (' + str(z) + ')')
    txtOutput = str(txtOutput) + str(str(x) + ': ' + str(y) + '% (' + str(z) + ')' + '\n')
    if int(z) > amtCheck:
        winner = str(x)
        amtCheck = int(z)
print('-------------------------')
print('Winner: ' + str(winner))
print('-------------------------')

outputFile = open('output.txt', 'w+')
outputFile.write('Election Results' + '\n')
outputFile.write('-------------------------' + '\n')
outputFile.write('Total Votes: ' + str(totalAmt) + '\n')
outputFile.write(txtOutput)
outputFile.write('-------------------------' + '\n')
outputFile.write('Winner: ' + str(winner) + '\n')
outputFile.write('-------------------------' + '\n')
outputFile.close()