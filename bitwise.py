#  W O R K     I N     P R O G R E S S

# Converts binary to decimal (without using python builtin)
def binDec(b):
    x = 0
    n = 0
    b = str(b)
    values = [i for i in range(len(b))]
    for c in b[::-1]:
        if c == '1':
            x += 2 ** values[n]
        n += 1
    return x

# Operates XOR on each bit of the two numbers, returning the result (without using ^ operator)
def XOR(n1, n2):
    l1 = [c for c in bin(n1)[2::]]
    l2 = [c for c in bin(n2)[2::]]
    
    if len(l1) != len(l2):
        if len(l1) > len(l2):
            for n in range(len(l1) - len(l2)):
                l2.insert(0, '0')
        elif len(l1) < len(l2):
            for n in range(len(l2) - len(l1)):
                l1.insert(0, '0')
    
    outList = []
    for i in range(len(l1)):
        if l1[i] == l2[i]:
            outList.append('0')
        else:
            outList.append('1')
    
    while outList[0] == '0':
        del outList[0]
        
    return binDec(''.join(outList))
