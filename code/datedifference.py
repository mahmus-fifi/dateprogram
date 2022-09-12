# program that gets the differece between two 
import datetime 
#print(dir(datetime))
#print(help(datetime))

# create variables 
start_date = datetime.datetime(2018,2,5)

end_date = datetime.datetime(2022, 9, 12)

months_in_a_year = 12 

# calculating the difference 
difference = (end_date.year - start_date.year) * months_in_a_year + (end_date.month - start_date.month)

# display the result 
print(f'the date difference from {start_date} to {end_date} is: {difference} months')

# displaying the results using a format specifier 
print("the date difference from %s to %s is: %s months" %(start_date, end_date, difference))