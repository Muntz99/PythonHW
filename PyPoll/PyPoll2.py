import os
import csv

csvpath = os.path.join('C:/Users/Muntz/Desktop/PythonHW/PyPoll/Resources/election_data.csv')
output_path = os.path.join("Output", "Election Results.txt")

Votes = []
Total_Votes = []
Candidates = []
Khan = []
Correy = []
Li = []
OTooley = []



with open(csvpath) as file:
    csvreader = csv.reader(file, delimiter =",")
    Header = next(csvreader)
        
    for row in csvreader:
        Votes.append(row[0])
        Total_Votes = len(Votes)
        Candidates.append(row[2])

    for candidate in Candidates:
            if candidate == "Khan":
                Khan.append(candidate)
                Khan_votes = (len(Khan))
                Can1 = "Khan"
            elif candidate == "Correy":
                Correy.append(candidate)
                Correy_Votes = (len(Correy))
                Can2 = "Correy"
            elif candidate == "Li":
                Li.append(candidate)
                Li_Votes = (len(Li))
                Can3 = "Li"
            else: 
                OTooley.append(candidate)
                OTooley_Votes = (len(OTooley))
                Can4 = "O'Tooley"

    KhanAve = round(((Khan_votes / Total_Votes) * 100), 2)
    Correy_Average = round(((Correy_Votes / Total_Votes)*100), 2)
    Li_Average = round(((Li_Votes / Total_Votes)*100), 2)
    OTooley_Average = round(((OTooley_Votes / Total_Votes)*100), 2)
    

    Winner = Candidates[(Votes.index(max(Votes)))]
    print(Winner)

    output = (
        f'Election Results\n'
        f'----------------------------\n'
        f'Total Votes: {Total_Votes}\n'
        f'{Can1}: {KhanAve}%  {Khan_votes}\n'
        f'{Can2}: {Correy_Average}%  {Correy_Votes}\n'
        f'{Can3}: {Li_Average}%  {Li_Votes}\n'
        f'{Can4}: {OTooley_Average}%  {OTooley_Votes}\n'
        f'----------------------------\n'
        f'The Winner is: {Winner}\n'

    )

    print(output)

with open(output_path, "w") as txt_file:
    txt_file.write(output)
    
#alternate trys
        # Total_Votes = Total_Votes + 1

    #     if row[2] not in Candidates:
    #         Candidates.append(row[2])
    #         Votes.append(0)
    #     Index = Candidates.index(row[2])
    #     Votes[Index] = Votes[Index] + 1
        
    # print(Total_Votes)
      
    # for i in Candidates:
    #     J = Candidates.index(i)
    #     #print(f"{Candidates[J]}: " "{:.2%}".format(Votes[J]/Total_Votes), (str(Votes[J])))
        
    #     voter_output = f"{Candidates[J]}: " "{:.2%}".format(Votes[J]/Total_Votes), (str(Votes[J])))
    #     print(voter_output)