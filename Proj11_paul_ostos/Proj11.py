#File: Proj11.py

'''
Among other things, this project requires you to 
 Read a csv file containing a large amount of stock market data.
 Extract specific values over a specific time period.
 Process the data.
 Display the processed data as colored lines on a line graph.
'''

from Proj11Runner import Runner
import sys

#Create and display a list of command-line arguments
args = sys.argv[1].split(",")
print()
print('args = ',args)
print()

print("Output from student code begins here.")
#Call the run method in the Runner file passing
#the args list as a parameter.
Runner.run(args)



