import matplotlib.pyplot as plt
import numpy

# Functions to compute and display the percentage frequency of any letter in a given plain/cipher text. 
# Useful for cryptanalysis.

def freqAnalyze(plaintext, graph = False):
    letters = {}
    total = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    for c in plaintext:
        if c in alphabet:
            if c not in letters:
                letters[c] = 1
            else:
                letters[c] += 1
        
            total += 1
    frequencies = {}
    
    for letter in letters:
        frequencies[letter] = (letters[letter] / total) * 100
        
    if graph:
        objects = frequencies.keys()
        ypos = numpy.arange(len(objects))
        
        plt.bar(ypos, frequencies.values(), align = 'center', alpha = 0.5)
        plt.xticks(ypos, objects)
        plt.ylabel('% of text')
        plt.title('letter frequency in text')

        plt.show()
        
    else:
        
        return frequencies
    
    
