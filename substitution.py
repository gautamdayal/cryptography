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

# creates a keyword based mapping. eg: 'julius caesar' returns j u l i s c a e r t v w x y z b d f ...
 def genKey(keyword):
    a = 'abcdefghijklmnopqrstuvwxyz'
    keylist = purify([c for c in keyword.lower()])
    x = ord(keylist[len(keylist) - 1]) - 97
    b = a[x:26] + a[0:x]
    for c in b:
        if c not in keylist:
            keylist.append(c)
    return(keylist)

# Implementation of the substitution cipher. Specify whether to print letter mapping by saying 'True' in optional arg.
# If a keyword based mapping is to be used, specify the word in the optional arg.
 def substitution(plaintext, keyword='', givekey = False):
    plaintext = plaintext.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    if keyword == '':
        L = randomAlpha()
    else:
        L = genKey(keyword)
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
        print('key: \n', mapping, '\n')    
    print('msg: ' + '\n' + ''.join(cipherList))
