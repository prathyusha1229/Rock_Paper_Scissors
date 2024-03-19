#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import secrets

game={1:"Rock",2:"Paper", 3: "Scissors"}
choice=int(input("Choose a number[1:Rock,2:Paper, 3: Scissors]:"))

computer=secrets.SystemRandom().randint(1,3)
print(f"{game[computer]}")

if choice==computer:
    print("draw")
elif (choice==1 and computer==3) or (choice==3 and computer==2) or (choice==2 and computer==1):
    print("You Won!")
else:
    print("OOPS, Computer Won")

