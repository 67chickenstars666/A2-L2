num=50
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