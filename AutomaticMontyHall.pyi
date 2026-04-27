#Need the ability to randomly sort
import matplotlib.pyplot as plt
import random
possibility="I need to define this ahead of time?"
j=0
w=0
k=0
switch=[]
stay=[]
while j<10000:
    #Necessary initial lists
    Doors= ["Car", "Goat", "Goat"]
    Keys=[0,1,2]
    #Results shuffle but the doors remain the same
    random.shuffle(Doors)
    #The first choice barely matters besides causing the paradoxical answer of 2 to 1
    k=random.randint(0,2)
    #The result for staying is created
    result=Doors[k]
    #K changes into its second role
    k=0
    if result=="Goat":
        possibility="Car"
    else:
        possibility="Goat"
    if possibility=="Car":
        w +=1
    switch.append(w / (j+1))
    #Reveal if won or loss. Well goat or car because goats are good aswell.
    #K takes it's final role as a restart button
    j +=1
print("Projected win rate:", 2/3)
print("Win rate:", w / j)
plt.plot(switch)
plt.title("See how close it gets")
plt.xlabel("Trials")
plt.ylabel("Success rate")
plt.axhline(2/3, color='r', linestyle='--')
plt.show()