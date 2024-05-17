
print("hello, welcome to lakshya pizza centre :")
print("which pizza would you like to have? s, m ,l ?")
size = input()
bill = 0
if size == "s":
  price = 200
elif size == "m":
  price = 300
elif size == "l":
  price = 100
else:
  print("please enter the correct size")

print(f"your {size} pizza cost ₹{price}")
cheese = input("do you want to add some cheese ? y or n ")
if cheese == "y":
  if size == "s":
    bill = price + 20
  else :
   bill = price + 30
else :
  bill = price
  

pepperoni = input("do you want to add some pepperoni? y or n ")

if pepperoni == "y" :
 if size == "s" :
   bill = bill + 20
 else :
   bill = bill + 30
else :
  bill = price

print(f"your final bill is ₹{bill}")



  
 



