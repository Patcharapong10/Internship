def checkprime(n):
    index = 0
    for i in range(2,n):
        if n%i == 0 :
            index = 0
            break
        else : 
            index = 1
    if index == 1 : return True
    else : return False

while True :
    numf = float(input("Input your number : "))
    #print(num)
    if numf > 1:
        for i in [10,100,1000]:
            if(checkprime(int(numf*i))):
                print("is prime")
                exit()
            else:
                print("is not prime")
            
    elif numf == 1 : print("is prime")
    else : exit()
