print("Welcome to Half Diamond!:")
# Taking input of number of rows
row = int(input("Enter number of rows: "))
# Checking if number of rows remainder is 0
if row%2==0:
    diamondrow = int(row/2)
else:
    diamondrow = int(row/2)+1
space = diamondrow-1
# This is the loop for upper part of the diamond
for i in range(1, diamondrow+1):
    for j in range(1, space+1):
        print(end=" ")
    space = space-1
    num = 1
    for j in range(2*i-1):
        print(end=str(num))
        num = num+1
    print()
space = 1
# This is the loop for lower part of the diamond
for i in range(1, diamondrow+1):
    for j in range(1, space+1):
        print(end=" ")
    space = space+1
    num = 1
    for j in range(1, 2*(diamondrow-i)):
        print(end=str(num))
        num = num+1
    print()