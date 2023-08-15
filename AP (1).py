import random

def ask():
    global a
    global d
    global n
    a=eval(input("Enter 1st (a) term= "))
    d=eval(input("CD (d)= "))
    n=eval(input("nth term of the AP= "))

def nt(a,d,n):
    t= a+ (n-1)*d
    print("nth term will be =",t)

def sumap(a,d,n):
    sum=0
    for i in range(1,n+1):
        z= a+ (i-1)*d
        sum=sum+z
        #print(z,end=" ")

    print("Sum of AP= ",sum) 

def randap():
    global d
    print("PLEASE SELECT A RANGE FOR DIFFERENCE")
    u=int(input("FROM :"))
    l=int(input("TO :"))
    n=int(input("Total No. of terms="))
    a=random.randint(1,50)
    d=random.randint(u,l)
    arg=str(input("Enter +/- sign for CD :"))
    print("TERMS are: ")
    if(arg=="-"):
        s=0
        while (n>1):
            z= a + (n-1)*d
            s=s+z
            print(z,end=' ')
            n=n-1
        print()
        print()
        print("CD is =","-",d)
        print("Sum of AP= ",s)
        
    elif(arg=="+"):
        for i in range(1,n+1):
            z= a+ (i-1)*d
            print(z,end=" ")
        print()
        print("CD is =",d)
        sumap(a,d,n)
        
print("CHOOSE INDEX NUMBER")
print("1) Calculate nth term of AP")
print("2) Calculate sum of an AP till nth term")
print("3) Generate a random AP and display it's sum")
x=str(input("INDEX? ="))

if (x=="1"):
    ask()
    nt(a,d,n)    
elif(x=="2"):
    ask()
    sumap(a,d,n)
elif(x=="3"):
    randap()
else:
    pass