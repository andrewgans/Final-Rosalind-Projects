#problem 2

def uracil():
    s = input()
    
    s = list(s)
    
    for i in range(len(s)):
        if s[i] == 'T':
            s[i] = 'U'
            
    seq1 = ""
    s = seq1.join(s)
          
    return s

print(uracil())