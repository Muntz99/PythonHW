import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')
output_path = os.path.join('Output', 'Final_Budget_Data.txt')


total = []
revenue = []
RevChanges = []
MonthChanges = []
Date = []
Months = []
Month = 0


with open(csvpath) as csvfile:
        csvreader = csv.reader(csvfile, delimiter =",")
        csv_header = next(csvreader)
        
        for row in csvreader:
                Months.append(row[0])
                revenue.append(row[1])

                Revenue_Int = map(int,revenue)
                total = sum(Revenue_Int)
                
                Month = len(Months)
      
        i = 0
        for i in range(len(revenue) - 1):
                profit_loss = int(revenue[i+1]) - int(revenue[i])
                RevChanges.append(profit_loss)
        totalrevchange = sum(RevChanges)

        AveChange = (totalrevchange / Month)

        GrtIncrease = max(RevChanges)
        K = RevChanges.index(GrtIncrease)
        MthIncrease_Line = Months[K + 1]

      
        LeastIncrease = min(RevChanges)
        J = RevChanges.index(LeastIncrease)
        MthDecrease_Line = Months[J + 1]


# print(f'Financial Analysis')
# print(f'----------------------------')
# print('Total Months: ' + str(len(Months)))
# print('Total: $' + str(total))
# print('Average Change: $' + str(round(AveChange, 2)))
# print(f'Greatest Increase in Profits: {MthIncrease_Line} (${GrtIncrease})')
# print(f'Greatest Decrease in Profits: {MthDecrease_Line} (${LeastIncrease})')
# print(f'----------------------------')


output = (
        f'Financial Analysis\n'
        f'----------------------------\n'
        f'Total Months: {Month}\n'
        f'Total: ${total}\n'
        f'Average Change: ${round(AveChange, 2)}\n'
        f'Greatest Increase in Profits: {MthIncrease_Line} ${GrtIncrease}\n'
        f'Greatest Decrease in Profits: {MthDecrease_Line} ${LeastIncrease}\n'
        f'----------------------------\n'
)

print(output)
with open(output_path, "w") as txt_file:
        txt_file.write(output)