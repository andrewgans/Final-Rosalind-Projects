def mating():
    values = input()
    values = values.split()
    
    k = int(values[0])
    m = int(values[1])
    n = int(values[2])
    
    total = k + m + n
    newtotal = total - 1
    
    #8 possible outcomes with dominant allele
    
    KK = ((k/total)*((k-1)/(newtotal)))
    KM = ((k/total)*(m/newtotal)) + ((m/total)*(k/newtotal))
    KN = ((k/total) * (n/newtotal)) + ((n/total)*(k/newtotal))
    MN = 0.5*(((m/total) * (n/newtotal)) + ((n/total)*(m/newtotal)))
    MM = 0.75*((m/total) * ((m-1)/newtotal))
    
    Probability = KK + KM + KN + MN + MM
    

    return Probability 

print(mating())
    