def count():
    s = input()
    
    Acount = 0
    Tcount = 0
    Ccount = 0
    Gcount = 0
    
    for i in range(len(s)):
        if s[i] == 'A':
            Acount += 1
        if s[i] == 'T':
            Tcount += 1
        if s[i] == 'C':
            Ccount += 1
        if s[i] == 'G':
            Gcount += 1
    final = [Acount,Ccount,Gcount,Tcount]
    
    print(*final)

count()