#GC content

def GCcontent(seq):
    #ident = input()
    #seq = input()
    
    seq = str(seq)
    
    GCount = 0
    
    seq = seq.replace(' ','')
    
    for i in range(len(seq)):
        if seq[i] == 'G' or seq[i] == 'C':
            GCount += 1
            
    percent = GCount/len(seq)
    
    percent = percent * 100
    
    percent = str(percent)
    
    #print(ident)        
    #print(float(percent[:9]))
    
    return (float(percent[:9]))



def fasta_to_dict(filename):
    with open(filename) as reader:
        lines = reader.read().splitlines()
        
    l = len(lines)
    i = 0
    d = {}
    
    while i < l:
        if lines[i][0] == '>':
            curr_ID = lines[i][1:]
            curr_str = ''
            i += 1
        while i < l and lines[i][0] != '>':
            curr_str += lines[i]
            i += 1
            
        d[curr_ID] = curr_str
                
    return d


def driver(d):
    results = len(d) * [0]
    i = 0 
    
    for key in d:
        results[i] = GCcontent(d[key])
        i += 1
    results = sorted(results)
    #print(d.keys())
    u = 0
    
    for key in d:
        if GCcontent(d[key]) == results[(len(d))-1]:
            print(key)

    return results[(len(d))-1]
print(driver(fasta_to_dict('rosalind_gc.txt')))
