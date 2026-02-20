#Grocery Billing System
a=int(input("Enter price of item 1: "))
b=int(input("Enter price of item 2: "))
c=int(input("Enter price of item 3: "))
total=a+b+c
discount=0
print("Total price: ",total)
if total>50:
   discount=total*0.1
   print("Discount applied: ",discount)
print("Final amount: ",total-discount)
