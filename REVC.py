#completing DNA problem

def complete():
    s = input()
    s = list(s)
    end = len(s) - 1
    
    complement = [''] * len(s)
    i = 0
    
    
    while end >= 0:
        if s[end] == 'G':
            complement[i] = 'C'
            end -= 1
            i += 1
            
        if s[end] == 'T':
            complement[i] = 'A'
            end -= 1
            i += 1

        if s[end] == 'C':
            complement[i] = 'G'
            end -= 1
            i += 1
     
        if s[end] == 'A':
            complement[i] = 'T'
            end -= 1
            i += 1
            
    seq1 = ""
    complement = seq1.join(complement)           
    
            
    print(complement)
    
complete()