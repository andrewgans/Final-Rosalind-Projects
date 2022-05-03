def wascally():
    inpt = input()
    inpt = inpt.split()
    
    n = int(inpt[0])
    k = int(inpt[1])
    
    rabbits = [0] * n
    
    rabbits[0] = 1
    rabbits[1] = 1
    
    i = 2
    
    for i in range(2,len(rabbits)):
        rabbits[i] = (rabbits[i-2] * k) + rabbits[i-1]
        
    return rabbits[n-1]

print(wascally())