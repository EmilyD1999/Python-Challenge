import csv

#Define variable values 
num_rows = 0
total_amount = 0
most_increase = 0
most_decrease = 0

increase_last_month = ''
increase_this_month = ''
decrease_last_month = ''
decrease_this_month = ''

total_change = 0
change_since_last_month = 0

#Open and link the correct corresponding data 
with open('Resources/budget_data.csv',"r") as csv_file:
    csv_read = csv.reader(csv_file, delimiter=',')
    
    #Find the number of rows so we know how many months there are 
    header = next(csv_read) 
    for row in csv_read:
        total_amount += int(row[1])
        num_rows += 1
 
 #Find the increase and ecrease by months 
        if num_rows > 1:
            change_since_last_month = int(row[1]) - amount_last_month
            if change_since_last_month > most_increase:
                most_increase = change_since_last_month
                increase_last_month = last_month
                increase_this_month = row[0]
            if change_since_last_month < most_decrease:
                decrease = change_since_last_month
                decrease_last_month = last_month
                decrease_this_month = row[0]
        
        #Define total change 
        total_change = total_change + change_since_last_month

        
        amount_last_month = int(row[1])
        last_month = row[0]


    print("Financial Analysis")
    print("------------------")
    print(f"Total months: {num_rows}")
    print(f"Total: {total_amount}")
    print(f"Average change: {round(total_change/(num_rows-1),2)}")
    print(f"Greatest increase in Profits: {most_increase} between {increase_last_month} and {increase_this_month}")
    print(f"Greatest decrease in profits: {most_decrease} between {decrease_last_month} and {decrease_this_month}")