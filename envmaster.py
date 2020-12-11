#envmaster.py
'''this is a program which will read a file and return its secrets'''


import os
import sys
import re







def envmaster():
    '''this script finds the  hidden .env folder and extracts the Discord token from it'''

    #This Regex gets everything between curley braces and returns it as a list
    regex = r"{([^}]*)}"
    with open(os.path.join(sys.path[0], ".env"), "r") as text:
        data = text.readlines()
    new = re.findall(regex, data[1], re.MULTILINE)
    secrets_revealed = new[0]
    print(secrets_revealed)
    return secrets_revealed

if __name__=='__main__':
    envmaster()

