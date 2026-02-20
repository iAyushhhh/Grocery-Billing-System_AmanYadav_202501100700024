print("Welcome to the store..........")
print()
a=int(input("Enter price of item 1: "))
b=int(input("Enter price of item 2: "))
c=int(input("Enter price of item 3: "))
total=a+b+c
discount=0
print()
print("\t\tTotal price: ",total)
if total>50:
   discount=total*0.1
   print(f"\t\tDiscount applied: {discount:.2f}")
print(f"\t\tFinal amount: {total-discount:.2f}")
print("\n")
print("\tThank you for shopping with us.......")
