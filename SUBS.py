#Finding a Motif

def motif():
    seq = input()
    subseq = input()
    
    i = 0
    p = len(subseq) - 1
    answer = [] * 3
    
    for i in range(len(seq)):
        p = len(subseq) + i
        if seq[i:p] == subseq:
            answer.append(i+1)
            
    print(*answer)
            
motif()