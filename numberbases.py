#  W O R K     I N     P R O G R E S S

# Converts binary to decimal
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
