#Need the ability to randomly sort
import random
#The first appearance of the universal key, k
k=-1
possibility="I need to define this ahead of time?"
while k==-1:
    #Necessary initial lists
    Doors= ["Car", "Goat", "Goat"]
    Keys=[0,1,2]
    #Results shuffle but the doors remain the same
    random.shuffle(Doors)
    #The first choice barely matters besides causing the paradoxical answer of 2 to 1
    while k!=0 and k!=1 and k!=2:
        #K's first real role
        k=int(input("Choose a door 0, 1 or 2}"))
    #The result for staying is created
    result=Doors[k]
    #I could probably work out the pops but it works well enough for now
    Doors.pop(k)
    Keys.pop(k)
    #K changes into its second role
    k=0
    while k<2:
        if Doors[k]=="Car":
            Doors.pop(k)
            Keys.pop(k)
            #The result for switching is created
            possibility="Car"
            break
        else:
            k +=1
    if len(Doors)==1:
        print("A goat has been revealed behind door", Keys[0])
    else:
        #The result for switching is once more created.
        possibility="Goat"
        #K takes its third role
        k=random.randint(0,1)
        print("A goat has been revealed behind door", Keys[k])
    #Final decision, switch or stay?
    while k!=3 and k!=4:
        #K takes its fourth role
        k=int(input("3 for keep door, 4 for switch doors}"))
    #Reveal if won or loss. Well goat or car because goats are good aswell.
    if k==3:
        print("You got the", result)
    else:
        print("You got the", possibility)
    #K takes it's final role as a restart button
    k=int(input("If want play again, enter -1:"))