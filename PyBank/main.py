import os 
import csv
#look for data we will be analyzing 
fileload = os.path.join("Resources","budget_data.csv")
#runway for the program to place a txt file where we want it to go 
outputfile = os.path.join("analysis", "PyBank.txt")  
#variable for months 
totalmonths = 0 #variable for months 
TotalProf_Loss = 0 #variable for net total profit/losses 
MonthlyChanges = [] # hold the monthly changes
months = [] #list to enter 
#read the file as csv 
with open(fileload) as Budget_data:
    csvreader = csv.reader(Budget_data)
    #calls the header 
    header = next (csvreader)
    #call the first row of actual data
    firstrow = next(csvreader)
    totalmonths += 1
    #add on to total profit 
    TotalProf_Loss += float(firstrow[1])
    #set the function to start on the first month's profit 
    previousprofit = int(firstrow[1]) 
    for row in csvreader:
        #increment count of total months 
        totalmonths += 1
        #add on to total profit 
        TotalProf_Loss += float(row[1])
        #calculates the change in profit
        profitchange = float(row[1]) - previousprofit
        #add the changes to the list 
        MonthlyChanges.append(profitchange)
        #adds first month that a change occurs
        months.append(row[0]) 
        previousprofit = float(row[1])
averageprofitchange = sum(MonthlyChanges) / len(MonthlyChanges)
#captures the month and profit of greatest increase
greatestprofitgain =[months[0],MonthlyChanges[0]] 
#captures the month and profit of greatest decrease
greatestprofitloss =[months[0],MonthlyChanges[0]] 
for g in range(len(MonthlyChanges)):
    #calculates if new value is greater than previous
    if(MonthlyChanges[g] > greatestprofitgain[1]):
        #if the value is greater then the new value becomes the greatestprofitgain
        greatestprofitgain[1] = MonthlyChanges[g]
        #updates month
        greatestprofitgain[0] = months[g]
    #calculates if new value is lesser than previous
    if(MonthlyChanges[g] < greatestprofitloss[1]):
        #if the value is lesser then the new value becomes the greatestprofitloss
        greatestprofitloss[1] = MonthlyChanges[g]        
        greatestprofitloss[0] = months[g]
# make the output 
output = ( 
    f"\nFinancial Analysis \n"
    f"-------------------------------------------------------------------------\n"
    f"Total Months:\t\t\t\t\t\t{totalmonths}"
    f"\nTotal:\t\t\t\t\t\t\t\t${TotalProf_Loss}"
    f"\nAverage Change:\t\t\t\t\t\t${averageprofitchange:,.2f}"
    f"\nGreatest Increase in Profits:\t\t{greatestprofitgain[0]} ${greatestprofitgain[1]:,.2f}"
    f"\nGreatest Decrease in Profits:\t\t{greatestprofitloss[0]} ${greatestprofitloss[1]:,.2f}"
)
#returns output information
print(output) 
#returns output information
with open(outputfile, "w") as textfile:  
    textfile.write(output)