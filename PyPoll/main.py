import os 
import csv
#loads the file of the election data
fileload = os.path.join("Resources","election_data.csv")
#ouputs a file with the elcetion analysis
outputfile = os.path.join("analysis", "PyPoll.txt")
#variable to hold.......
numberofvotes = 0 #number of votes
candidates = [] #a list of each candidate
candidvotes = {} #dictionary of how many votes each candidate recieved
winningvotecount = 0 #the winning vote count
winningcandidate= 0 #the name of the winning candidate

#read the csv file
with open(fileload) as election_data:
    #create the csv reader
    csvreader = csv.reader(election_data)
    #reads the header
    header = next(csvreader)

    #function reads each row
    for row in csvreader:
        #counts the first row and adds 1 for every row after
        numberofvotes += 1
        # reads each row to see if candidate is not on the "candidate[]" list
        if row[2] not in candidates:
             #adds candidate to list 
            candidates.append(row[2])
            #starts the count for each candidate at 1 
            candidvotes[row[2]] = 1
        else:
            #adds one to the candidates vote 
            candidvotes[row[2]] += 1

#variable to hold results for the candidates
voteroutput = ""
#loop through the candidates vote counts
for candidates in candidvotes:
    #gets the vote count for each candidate and store it in "votes"
    votes = candidvotes.get(candidates)
    #find the percentage of votes each candidate received, store in "votepct'"
    votepct = (float(votes)/ float(numberofvotes)) * 100.00
    #output the candidates name with percentage of votes and vote count
    voteroutput += f"{candidates}:\n\t\t{votepct:.2f}% ({votes})\n\t\t---------------|\n"

    #compares the votes for each candidate to see who has a higher vote count
    if votes > winningvotecount:
        #updates "votes" to "winningvotecount" that will hold the highest count of votes
        winningvotecount = votes
        #updates "candidates" variable to "winningcandidate" that will hold the name of the candidate with most votes
        winningcandidate = candidates

#variable to hold all the outputs
output = (
    f"\n\t\tElection Results\n"
    f"----------------------------------------------\n"
    f"Total votes:\t{numberofvotes:,}\n"
    f"----------------------------------------------\n"
    f"{voteroutput}\n"
    f"----------------------------------------------\n"
    f"\tWinner Winner Chicken Dinner:\n\t\t {winningcandidate}\n"
    f"----------------------------------------------\n"
)
#print output into the PyPoll.txt file
print(output)
with open(outputfile, "w") as textfile:
    textfile.write(output)   