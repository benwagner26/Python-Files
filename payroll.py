"""
Program: payroll.py
Project 4.12

Print a payroll report.

Input
   A file in which each line has the form
   
   <last name> <hourly wage> <hours worked>

Output
   A report in tabular format.  Each line has the form

   <last name> <hours worked> <total wages>
   
"""

# Take the inputs
fileName = input("Enter the file name: ")

# Open the input file
inputFile = open(fileName, 'r')

# Read the data and print the report
print(f"{'Name' : <10}{'EmpNUm' : <10}{'Address' : <30}{'Hours' : <10}{'Total Pay' : <10}")

for line in inputFile:
   dataList = line.split()
   name = dataList[0]
   empNum = int(dataList[1])
   address = dataList[2]
   hours = int(dataList[3])
   payRate = float(dataList[4])
   totalPay = hours * payRate
   print(f"{name : <10}{empNum : ^10}{address : <30}{hours : <10}{totalPay : <10}")


  
# printing values of variables in Aligned manner
