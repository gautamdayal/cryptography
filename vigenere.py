# Implementation of the vigenere cipher

def charVal(c):
    return ord(c) - 96

# User specifies action argument as 'e' for encryption and 'd' for decryption. Defaults to 'e'
def vigenere(plaintext, keyword, action):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    keyword = keyword.lower()
    if action == 'e':
        keylist = [charVal(c) for c in keyword]
    elif action == 'd':
        keylist = [-charVal(c) for c in keyword]
        
    cipherlist = []
    i = 0
    length = len(keylist)
    
    for c in plaintext: 
        cursor = i % length
        
        if c in alphabet:
            cipherlist.append(alphabet[(charVal(c) + keylist[cursor]) % 26 - 1])
        else:
            cipherlist.append(c)
        i += 1
        
    return ''.join(cipherlist)
