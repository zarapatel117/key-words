print("Hi, you have some amount pending to pay")
amountpayed=int(input("Enter the amount you payed: "))
bill= int(input("Enter the total amount to be payed: "))

if amountpayed < bill:
    print("Amount due is" ,bill-amountpayed)
elif amountpayed == bill:
    print("payed")
    pass
else:
    print(" oh You payed extra ")