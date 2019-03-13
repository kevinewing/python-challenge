#PyPoll/main.py
import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")

totalVotes = 0
KhanVotes = 0
CorreyVotes = 0
LiVotes = 0
OTooleyVotes = 0
OtherVotes = 0

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    
    for row in csvreader:
        if row[2] == "Khan":
            KhanVotes += 1
        elif row[2] == "Correy":
            CorreyVotes += 1
        elif row[2] == "Li":
            LiVotes += 1
        elif row[2] == "O'Tooley":
            OTooleyVotes += 1
        else:
            OtherVotes += 1

totalVotes = KhanVotes + CorreyVotes + LiVotes + OTooleyVotes + OtherVotes
khanpercent = (KhanVotes / totalVotes) *100
correypercent = (CorreyVotes / totalVotes) *100
lipercent = (LiVotes / totalVotes) *100
otooleypercent = (OTooleyVotes / totalVotes) *100
otherpercent = (OtherVotes / totalVotes) *100


largest = max(KhanVotes, CorreyVotes, LiVotes, OTooleyVotes, OtherVotes)

if largest == KhanVotes:
    winner = "Khan"
elif largest == CorreyVotes:
    winner = "Correy"
elif largest == LiVotes:
    winner = "Li"
elif largest == OTooleyVotes:
    winner = "O'Tooley"
elif largest == OtherVotes:
    winner = "Other"
    

print("Election Results")
print("-------------------------")
print("Total Votes: " + str(totalVotes))
print("-------------------------")
print("Khan: " + str(format(khanpercent,".3f")) + "% (" + str(KhanVotes) + ")")
print("Correy: " + str(format(correypercent,".3f")) + "% (" + str(CorreyVotes) + ")")
print("Li: " + str(format(lipercent,".3f")) + "% (" + str(LiVotes) + ")")
print("O'Tooley: " + str(format(otooleypercent,".3f")) + "% (" + str(OTooleyVotes) + ")")
print("-------------------------")
print("Winner: " + str(winner))
print("-------------------------")

output_path = os.path.join("output.csv")
with open(output_path,'w' , newline='') as csvoutputfile:
    csvwriter = csv.writer(csvoutputfile, delimiter=',')
    csvwriter.writerow(["Khan Votes:", KhanVotes, khanpercent])
    csvwriter.writerow(["Correy Votes:", CorreyVotes, correypercent])
    csvwriter.writerow(["Li Votes:", LiVotes, lipercent])
    csvwriter.writerow(["O'Tooley Votes:", OTooleyVotes, otooleypercent])
    
