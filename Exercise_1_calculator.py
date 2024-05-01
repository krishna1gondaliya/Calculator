

val1 = int(input("Enter any number"))

val2 = int(input("Enter another number"))

operator_selection = int(input("For Addition press 1 \nFor Substraction press 2 \nFor Division press 3 \nFor Multiplication press 4 \n"))

#error handeling


if operator_selection==1:
    addition = val1+val2
    print(addition)

if operator_selection==2:
    substraction = val1-val2
    print(substraction)

if operator_selection==3:
    division = val1/val2
    print(division)

if operator_selection==4:
    multiplication = val1*val2
    print( multiplication)

#error handeling
if operator_selection>=5:
    print("Please enter number corresponding to the operator")


    
