#Need the ability to randomly sort
import random
#The first appearance of the universal key, k
k=-1
possibility="I need to define this ahead of time?"
while k==-1:
    #Necessary lists
    Doors= ["Car", "Goat", "Goat"]
    Keys=[0,1,2]
    random.shuffle(Doors)
    while k!=0 and k!=1 and k!=2:
        k=int(input("Choose a door 0, 1 or 2}"))
    result=Doors[k]
    Doors.pop(k)
    Keys.pop(k)
    #K changes into its second role
    k=0
    while k<2:
        if Doors[k]=="Car":
            Doors.pop(k)
            Keys.pop(k)
            possibility="Car"
            break
        else:
            k +=1
    if len(Doors)==1:
        print("A goat has been revealed behind door", Keys[0])
    else:
        possibility="Goat"
        #K takes its third role
        k=random.randint(0,1)
        print("A goat has been revealed behind door", Keys[k])
    while k!=3 and k!=4:
        #K takes its fourth role
        k=int(input("3 for keep door, 4 for switch doors}"))
    if k==3:
        print("You got the", result)
    else:
        print("You got the", possibility)
    #K takes it's final role as a restart button
    k=int(input("If want play again, enter -1:"))