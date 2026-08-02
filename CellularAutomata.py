#Important imports
import numpy as np
import random
import time
#3 variables that are needed for cells
left=1
center=1
right=1
#The two arrays needed. 
z=np.array([0]*20)
z=[random.randint(0,1) for y in range(20)]
arrayread=np.array([0]*20)
#This is currently a rule 50 model. I may switch to a varying system later. So that the rule is randomized. 
try:
    while True:
        time.sleep(.2)
        print(z)
        for x in range(20):
            if x!=0:
                left=z[x-1]
            else:
                left=z[19]
            if x!=19:
                right=z[x+1]
            else:
                right=z[0]
            middle=z[x]
            if middle==0:
                if left==1 and right==0:
                    arrayread[x]=1
                elif left==0 and right==0:
                    arrayread[x]=0
                else:
                    arrayread[x]=1
            else:
                arrayread[x]=0
        for i in range(20):
            z[i]=int(arrayread[i])
except KeyboardInterrupt:
    print("Take a break")