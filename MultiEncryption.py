# Assignment 4 Question 1

import EncryptTechnique as ET

n = 8   # public number for A (client)
q = 5   # public number for B (server)

def computeKeyEncrypt(privateNum):
# y = n^x mod q, where x is the private number for server/client
    return (n**privateNum)%q
    
def computeKeyDecrypt(recvVal, privateNum):
    return ((recvVal**privateNum)%q)
    
def Encrypt(string, order):
    retString = string
    for i in range(2):
        if order[i] == "0":
            retString = ET.TranspositionEncrypt(retString)
        elif order[i] == "1":
            retString = ET.SubstitutionEncrypt(retString, 1)
        elif order[i] == "2":
            retString = ET.SubstitutionEncrypt(retString, 2)
        else:
            retString = ET.SubstitutionEncrypt(retString, 3)
    return retString
    
def Decrypt(string, order):
    retString = string
    for i in range(2):
        if order[1-i] == "0":
            retString = ET.TranspositionDecrypt(retString)
        elif order[1-i] == "1":
            retString = ET.SubstitutionDecrypt(retString, 1)
        elif order[1-i] == "2":
            retString = ET.SubstitutionDecrypt(retString, 2)
        elif order[1-i]: 
            retString = ET.SubstitutionDecrypt(retString, 3)
    return retString
    
def getSchemeOrder(key):
    if key == 0:
        order = "01"
    elif key == 1:
        order = "02"
    elif key == 2:
        order = "03"
    elif key == 3:
        order = "11"
    else: # key == 4
        order = "22"
    return order
    
def main():
    hiddenKey = computeKeyEncrypt(6)
    print(computeKeyDecrypt(hiddenKey, 6))
    print(computeKeyDecrypt(hiddenKey, 4))
      
if __name__=="__main__":
    main()