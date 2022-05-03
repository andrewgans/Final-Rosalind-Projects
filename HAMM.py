#Point Mutations

def mutatecheck():
    firstsequence = input()
    secondsequence = input()
    
    i = 0
    count = 0
    
    for i in range(len(firstsequence)):
        if firstsequence[i] != secondsequence[i]:
            count += 1
    return count

print(mutatecheck())