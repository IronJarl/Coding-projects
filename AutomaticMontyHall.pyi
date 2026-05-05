#Need the ability to randomly sort and graph
import matplotlib.pyplot as plt
import random
possibility="I need to define this ahead of time?"
j=0
w=0
k=0
switch=[]
n=0
while n <= 0:
    n=int(input("Positive value for tests:"))
while j<n:
    #Necessary initial lists
    Doors= ["Car", "Goat", "Goat"]
    Keys=[0,1,2]
    #Results shuffle but the doors remain the same
    random.shuffle(Doors)
    #The first choice barely matters besides causing the paradoxical answer of 2 to 1
    #Could probably automize to 1 but this shows that randomness remains true
    k=random.randint(0,2)
    #The result for staying is created
    result=Doors[k]
    k=0
    if result=="Goat":
        possibility="Car"
    else:
        possibility="Goat"
    if possibility=="Car":
        w +=1
    #The win rate is naturally wins/tries and since tries=j+1 in this context
    switch.append(w / (j+1))
    j +=1
#Once more got a lot of this actual graphing from an outside source. Mostly me though
print("Projected win rate:", 0.6666666666666666)
print("Overall Win rate:", w / j)
plt.plot(switch)
plt.title("See how close it gets")
plt.xlabel("Trials")
plt.ylabel("Success rate")
plt.axhline(2/3, color='r', linestyle='--')
plt.show()
#If wonder how it works for staying consistently, it's just 1-SwitchWin=StayWin