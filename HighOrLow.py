import random
#k is for key, d is for door, t is for amount of guesses, inputs shows all different tries.
d=random.randint(1,10000)
t=1
inputs=[]
k=int(input("Pick a number, 1 through 10000:"))
inputs.append(k)
while k != d:
    #Wasted guess prevention
    if k>=1 and k<=10000:
        #Basic feedback loop
        if k>d:
            k=int(input("Lower:"))
            inputs.append(k)
            t +=1
        else:
            k=int(input("Higher:"))
            inputs.append(k)
            t +=1
    else:
        k=int(input("Invalid number. Enter new number:"))
#Important data after a game well done.
print("solution",k)
print("You win!!!!")
print("Tries:", t)
print("Guesses:", inputs)