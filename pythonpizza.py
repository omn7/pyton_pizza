print('''
           
 _ __  _ __________ _ 
| '_ \| |_  /_  / _` |
| |_) | |/ / / / (_| |
| .__/|_/___/___\__,_|
| |                   
|_|                   ''')

print("welcome to the pizza hurt")
pepperoni = "2"
Extra_cheese = "1"
M = 10
S = 5
L = 15
cheese = 1
bill = 0

choise1 = input("choose the size of the pizza 'M' 'L' 'S' ")
if choise1 == "S":
  pepperoni = input("do you want pepperoni 'Y' or 'N' :- ")
  if pepperoni == "Y":
    cheese = input("need extra cheesse 'Y' or 'N' ")
    if cheese == "Y":
      print(S + 2 + 1)
    else:
      print(f"it will cost you {S}")  
  else:
   cheese = input("need extra cheesse 'Y' or 'N' ")
   if cheese == "Y":
      print(S + 1)
   else:
     print(f"it will cost you  ")   



if choise1 == "M":
  pepperoni = input("do you want pepperoni 'Y' or 'N' :- ")
  if pepperoni == "Y":
    cheese = input("need extra cheesse 'Y' or 'N' ")
    if cheese == "Y":
      
      print(M + 2 + 1)
    else:
      cheese = input("need extra cheesse 'Y' or 'N' ")
    if cheese == "Y":
      print(M + 1)
  else:
    cheese = input("need extra cheesse 'Y' or 'N' ")
  if cheese == "Y":
      print(S + 1)
  else:
     print(f"it will cost you  ") 

 

elif choise1 == "L":
  pepperoni = input("do you want pepperoni 'Y' or 'N' :- ")
  if pepperoni == "Y":
    print(L + 3)
  else:
    print(f"it will cost you {L}")

else:
  print("error not found any pizza")    
