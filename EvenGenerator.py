#Cannot forget the time, don't want to burn out the computer
import time
def Even():
     #0 is in fact an even number despite it's appearance
     num=0
     amount=0
     while True:
            time.sleep(.1)
            #I believe this is the basis of all generators so it's needed
            yield num
            num +=2
try:
    for value in Even():
        print(value)
#Can't forget about the escape route
except KeyboardInterrupt:
    print("That's enough")
    print("Amount generated:", int(1+value/2))