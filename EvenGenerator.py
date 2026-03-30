
import time
def Even():
     num=0
     while True:
            time.sleep(.1)
            yield num
            num +=2
try:
    for value in Even():
        print(value)
except KeyboardInterrupt:
    print("That's enough")