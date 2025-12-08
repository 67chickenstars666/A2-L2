num=3
if num > 0:
    print("Positive number")
num=-1
if num < 0:
    print("Negative number")
    actual_cost=float(input("Please enter the actual cost: "))
    sale_amount=float(input("Please enter the sale amount: "))
    if sale_amount > actual_cost:
        amount=sale_amount-actual_cost
        print("Total profit= {0}".format(amount))
    else:
        print("No Profit :(")
# checking the number greater or smaller than fifteen
i=int(input("enter a number: "))
if (i<15):
    print("number is smaller than 15")
else:
    print("number is greater than 15")
    print("I'm in else block")
print("I'm out of else block ")
number = int(input("Enter a number to check: "))
print("Number to be checked :", number)
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")