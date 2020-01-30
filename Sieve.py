import math
import time
import os
import random

def eratos(n,s = None):
    if s is not None:
        a = []
        
        for i in range(n):
            a.append(True)
        
        a[0]= False
        
        for i in range((int)(math.sqrt(n))):
            if a[i+2] == True:
                for j in range(((i+2)**2), n, (i+2)):
                    a[j] = False
        
        for i in range(n):
            if i < s:
                a[i] = False

        primes = []
        
        for i in range(n):
            if a[i] == True:
                primes.append(i)

        return primes
        
    else:
        a = []
        
        for i in range(n):
            a.append(True)
        
        a[0]= False
        
        for i in range((int)(math.sqrt(n))):
            if a[i+2] == True:
                for j in range(((i+2)**2), n, (i+2)):
                    a[j] = False
        
        primes = []
        
        for i in range(n):
            if a[i] == True:
                primes.append(i)
        
        primes.remove(1)
        return primes
        
def eratosthenes(n,s = None):
    if s is not None:
        start = time.time()
        a = []
        
        for i in range(n):
            a.append(True)
        
        a[0]= False
        
        for i in range((int)(math.sqrt(n))):
            if a[i+2] == True:
                for j in range(((i+2)**2), n, (i+2)):
                    a[j] = False
        
        for i in range(n):
            if i < s:
                a[i] = False

        primes = []
        
        for i in range(n):
            if a[i] == True:
                primes.append(i)
           
        print(primes)
        end = time.time()
        print("Execution time: " + str(round(end - start, 3)))
        
    else:
        start = time.time()
        a = []
        
        for i in range(n):
            a.append(True)
        
        a[0]= False
        
        for i in range((int)(math.sqrt(n))):
            if a[i+2] == True:
                for j in range(((i+2)**2), n, (i+2)):
                    a[j] = False
        
        primes = []
        
        for i in range(n):
            if a[i] == True:
                primes.append(i)
        
        primes.remove(1)
        print(primes)
        end = time.time()
        print("Execution time: " + str(round(end - start, 3)))
        
def sundaram(n,s = None):
    if s is not None:
        start = time.time()
        n += 2
        s += 2
        a = []

        if n % 2 == 0:
            new = (int)(((n-2)/2))
        else:
            new = (int)((((n-2)/2)) + 0.5)
        
        for i in range(new):
            a.append(True)

        for i in range(1, new+1):
            j = i
            while(i+j+2*i*j < new):
                a[i+j+2*i*j] = False
                j += 1
        
        if s % 2 == 0:
            sNew = (int)(((s-2)/2))
        else:
            sNew = (int)((((s-2)/2)) + 0.5)
            
        for i in range(new):
            if i < sNew:
                a[sNew] = False

        for i in range(new):
            if i < sNew:
                a[i] = False
        
        primes = []
            
        for i in range(1,new):
            if a[i] == True:
                primes.append((i*2)+1)

        print(primes)
        end = time.time()
        print("Execution time: " + str(round(end - start, 3)))
        
    else:
        start = time.time()
        n += 2
        a = []

        if n % 2 == 0:
            new = (int)(((n-2)/2))
        else:
            new = (int)((((n-2)/2)) + 0.5)
        
        for i in range(new):
            a.append(True)

        for i in range(1, new+1):
            j = i
            while(i+j+2*i*j < new):
                a[i+j+2*i*j] = False
                j += 1

        primes = []

        if n >= 2:
            primes.append(2)
            
        for i in range(1,new):
            if a[i] == True:
                primes.append((i*2)+1)

        print(primes)
        end = time.time()
        print("Execution time: " + str(round(end - start, 3)))

def runProgram():
    p = eratos(100000,10000)
    l = len(p)
    rpone = p[random.randint(0,l)]
    rptwo = p[random.randint(0,l)]

    os.chdir("/Users/903610/Desktop/")
    n = random.randint(0,999)
    name = "Primes" + str(n)
    os.mkdir(name)
    newdir = "/Users/903610/Desktop/" + name
    os.chdir(newdir)
    fname = "output" + str(n) + ".txt"
    print("Index#:" + str(n))
    
    with open (fname, "w") as f:
        f.write(str(rpone) + ", " + str(rptwo))

    key = rpone * rptwo
    print("The key is " + str(key))
    a = input("Enter key one: ")
    b = input("Enter key two: ")
    a = (int)(a)
    b = (int)(b)
    if (key / a) / b == 1:
        print("Access Granted!")
    else:
        print("Access Denied.")

print("choose either of two prime number finders using")
print("eratosthenes(n) or sundaram(n). You can also")
print("use eratosthenes(m,n) or sundaram(m,n) to find")
print("all the primes between n and m.")
print("")
print("type runProgram() to use the finished program.")
print("the keys (numbers) will appear on the desktop.")
print("typing in the right keys will print Access Granted.")
print("typing in the wrong keys will print Access Denied.")
    
