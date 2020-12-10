import csv 
all_candidates = []
vote_count = []

#Define the data we are working with as election_data.csv
#Create an if statement that adds together the amount of votes every canditdate got 
with open("Resources/election_data.csv") as csv_file:
    csv_read = csv.reader(csv_file, delimiter=',')
    header = next(csv_read)
    for row in csv_read:
        if row[2] not in all_candidates:
            all_candidates.append(row[2])
            vote_count.append(1)
        else:
            whatindex = all_candidates.index(row[2])
            vote_count[whatindex] += 1

#Define total votes 
    total_votes = sum(vote_count)
#Define vote percentage 
    votepercentage = [round(vote_count[i]/total_votes*100,4) for i in range(0,len(vote_count))]

#Print Results from table 
    print("--------------------")
    print("| Election Results |")
    print("--------------------")
    print(f"Total Votes: {total_votes}")
    print("--------------------")

    #Print all candidates with their name, vote count and vote percentage 
    for i in range(0,len(all_candidates)):
        print(f"Candidate: {all_candidates[i]} with {vote_count[i]} votes ({votepercentage[i]}%)")

#Print winner of election by finding the person with the max amount of votes
    print("--------------------")
    print(f"The winner is: {all_candidates[vote_count.index(max(vote_count))]}")
