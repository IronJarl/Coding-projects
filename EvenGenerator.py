#Cannot forget the time, don't want to burn out the computer
import time
def Even():
     #0 is in fact an even number despite it's appearance
     num=0
    #Since it can't be false, it shall go on forever.
    #Until the heat death of the universe or processing issues, whichever is first.
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
    #I found this to be the easiest way to show the amount generated
    print("Amount generated:", 1+value//2)