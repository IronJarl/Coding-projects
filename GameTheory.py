import random
import matplotlib.pyplot as plt
a=0
b=0
c=0
d=0
k=1
j=0
P1Choice="Yellow"
P2Choice="Zinger"
P1Score=0
P2Score=0
P1ScoreStuff=[]
P2ScoreStuff=[]
def RandomStrat():
     a=random.randint(0,10000)
     if a!=0:
         b=random.randint(a,10000)
     else:
         b=1
     return a/b
c=RandomStrat()
d=RandomStrat()
while k<=10000:
     j=random.uniform(0,1)
     #It was difficult finding out if it should be inclusive towards stealing or towards sharing
     if j<=c:
        P1Choice="Steal"
     else:
        P1Choice="Share"
     j=random.uniform(0,1)
     if j<=c:
         P2Choice="Steal"
     else:
         P2Choice="Share"
     if P1Choice=="Steal":
          if P2Choice=="Steal":
              P1Score +=1
              P2Score +=1
          else:
              P1Score +=5
     else:
         if P2Choice=="Steal":
             P2Score +=5
         else:
             P1Score +=3
             P2Score +=3
     P1ScoreStuff.append(P1Score / (5*k))
     P2ScoreStuff.append(P2Score / (5*k))
     k +=1
print("Probability of stealing for Player 1:", c)
print("Probability of stealing for Player 2:", d)
print("Overall payout for Player 1:", P1ScoreStuff[(len(P1ScoreStuff)-1)])
print("Overall payout for Player 2:", P2ScoreStuff[(len(P2ScoreStuff)-1)])
plt.plot(P1ScoreStuff)
plt.plot(P2ScoreStuff)
plt.title("Average payoff")
plt.xlabel("Trials")
plt.ylabel("Percentage of total won")
plt.axhline(3/5, color='r', linestyle='--')
plt.axhline(1/5, color='b', linestyle='--')
plt.show()