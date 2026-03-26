#Time is absolutely required to not fry the device
import time
#No use checking for a prime number less than 2
y=1
prime=[2]
try:
    while True:
        time.sleep(0.1)
        y +=2
        z=0
        while True:  
             #Basic modular division to check for remainder, it's much easier for a computer this way"      
            if z==len(prime)-1 or prime[z]**2>y: #Applying theorem of composite numbers and a factor less than or equal to it's root
                #Got rid of my key idea, it was slow
                prime.append(y)
                break
            elif y%prime[z] == 0:
                break
            else:
                z +=1
#Escape method once you have let it run long enough
except KeyboardInterrupt:
    #List and other important bits of info
    print(prime)  
    print(f"Amount of primes found: {len(prime)}")
    print(f"Largest prime: {prime[-1]}")