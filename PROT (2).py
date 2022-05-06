#PROT problem - already done beforehand which is why theres so much extra code 
def inputseq():

    seq = (input())
    return(seq)


aacids = {}
aacids ={'END':'END','UUU':'F','CUU':'L','AUU':'I','GUU':'V','UUC':'F','CUC':'L','AUC':'I','GUC':'V','UUA':'L','CUA':'L','AUA':'I','GUA':'V','UUG':'L','CUG':'L','AUG':'M','GUG':'V','UCU':'S','CCU':'P','ACU':'T','GCU':'A','UCC':'S','CCC':'P','ACC':'T','GCC':'A','UCA':'S','CCA':'P','ACA':'T','GCA':'A','UCG':'S','CCG':'P','ACG':'T','GCG':'A','UAU':'Y','CAU':'H','AAU':'N','GAU':'D','UAC':'Y','CAC':'H','AAC':'N','GAC':'D','UAA':'Stop','CAA':'Q','AAA':'K','GAA':'E','UAG':'Stop','CAG':'Q','AAG':'K','GAG':'E','UGU':'C','CGU':'R','AGU':'S','GGU':'G','UGC':'C','CGC':'R','AGC':'S','GGC':'G','UGA':'Stop','CGA':'R','AGA':'R','GGA':'G','UGG':'W','CGG':'R','AGG':'R','GGG':'G'}



def amino(cd):
    if len(cd) == 0:
        return 'END'
    else:
        singlecodon = cd[0:3]
        restacids = cd[3:]
        singleacid = aacids[singlecodon]
        finalrestacids = amino(restacids)
    Acids = singleacid + finalrestacids
    Acids = Acids.replace('ENDEND','')
    Acids = Acids.replace('Stop','')
    return Acids
        
    
#print(amino(codons(cleanup(inputseq()))))


def newamino(seq):
    i = 0
    u = 0
    codons = [''] * 0
    
    for u in range(0,len(seq)//3):
        cdn = seq[i:i+3]
        codons.append(cdn)
        i += 3
    return codons

def newproteins(codonlist):
    #print(codonlist)
    #singlecodon = codonlist[0]
    #print(aacids[codonlist[0]])
    
    for i in range(len(codonlist)):
        codonlist[i] = aacids[codonlist[i]]
        
        Acids = codonlist
        Acids = ''.join(Acids)
        Acids = Acids.replace('Stop','')
        
    print(Acids)

newproteins(newamino(inputseq()))