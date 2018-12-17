# generates a string made up of lower and uppercase characters, numbers, special characters
# note to self: add file I/O

from random import *

def generatePassword(lowerN, upperN, nN, specialN):
  
  specials = '!@#$%^&*?'
  lowers = 'abcdedfhijklmnopqrstuvwxyz'
  uppers = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  generated = []
  passwordList = []
  passwordString = None

  for n in range(lowerN):
    passwordList.append(lowers[randint(0, len(lowers)-1)])
  
  for n in range(upperN):
    passwordList.append(uppers[randint(0, len(uppers)-1)])
  
  for n in range(nN):
    passwordList.append(str(randint(0,9)))
  
  for n in range(specialN):
    passwordList.append(specials[randint(0,len(specials)-1)])

  passwordString = ''.join(passwordList)

  return passwordString
  
