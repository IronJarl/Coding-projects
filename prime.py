#Time is absolutely required to not fry the device
import time
#No use checking for a prime number less than 2
y=3
prime=[2]
try:
    while True:
        time.sleep(0.1)
        z=0
        #K for key, how clever
        k=0
        #Applying the theorem of "composite number must have a prime factor no greater than it's square root"
        while prime[z]**2<=y:  
            #Basic modular division to check for remainder, it's much easier for a computer this way"      
            if y%prime[z]==0:
                k=1
                break
            elif z==len(prime)-1:
                break
            else:
                z +=1
        #The door to primehood
        if k==0:
            prime.append(y)
        #Count by twos since all even numbers are naturally composite
        y +=2
#Escape method once you have let it run long enough
except KeyboardInterrupt:
    #List and other important bits of info
    print(prime)  
    print(f"Amount of primes found: {len(prime)}")
    print(f"Largest prime: {prime[-1]}")