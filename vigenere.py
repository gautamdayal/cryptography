# Implementation of the vigenere cipher

def charVal(c):
    return ord(c) - 96

# User specifies action argument as 'e' for encryption and 'd' for decryption.
def vigenere(plaintext, keyword, action):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    keyword = keyword.lower()
    
    if action == 'e':
        keylist = [charVal(c) for c in keyword]
    elif action == 'd':
        keylist = [-charVal(c) for c in keyword]
    else:
        print('enter e for encrypt and d for decrypt')
        
    cipherlist = []
    i = 0
    length = len(keylist)
    
    for c in plaintext: 
        cursor = i % length

        if c.isalpha():
            cipherlist.append(alphabet[(charVal(c) + keylist[cursor]) % 26 - 1])
        else:
            cipherlist.append(c)
        i += 1
        
    return ''.join(cipherlist)
