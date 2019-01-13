# Produces a list containing the alphabet in a randomized, scrambled order.
def randomAlpha():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    p = [c for c in alphabet]
    c = []
    while len(c) != 26:
        x = random.randint(0, len(p) - 1)
        c.append(p[x])
        p.remove(p[x])
    return c
    
# Implementation of the substitution cipher. Specify whether to print letter mapping by saying 'True' in optional arg.
def substitution(plaintext, givekey = False):
    plaintext = plaintext.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    L = randomAlpha()
    mapping = {}
    
    for i in range(26):
        mapping[alphabet[i]] = L[i]
    cipherList = []
    
    for c in plaintext:
        if c in alphabet:
            cipherList.append(mapping[c])
        else:
            cipherList.append(c)
            
    if givekey:
        print('key: ', mapping)    
        
    print('msg: '+ ''.join(cipherList))
