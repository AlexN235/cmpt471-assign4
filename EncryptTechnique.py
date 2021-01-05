#$!/usr/bin/env python3

from enum import Enum
from array import *

def SubstitutionEncrypt(str, schemeNum):
    #schemeNum = 1
    encryptionKey = initEncryptArr()
    data = ""
    for i in str:
        if i not in encryptionKey[0]:
            data += i
            continue
        index = encryptionKey[0].index(i)
        val = encryptionKey[schemeNum][index]
        data += val
    return data
    
def TranspositionEncrypt(str):
# Cuts the plaintext into segments, each segment a string of r x n characters
    retStr = ''
    size, iter = numOfSegments(str)
    arrSize = size*size
    # Puts the string of characters into an r x n array A
    for i in range(iter):
        if i == iter:
            smallString = str[i*arrSize : len(str)-1]
        else:
            smallString = str[i*arrSize : (i+1)*arrSize]
            
        retStr += readArr(rearrageString(smallString, size))
    # Reads the array from top to bottom and columns from left to right.
    return retStr
    
def SubstitutionDecrypt(str, schemeNum):
    #schemeNum = 1
    arr = initDecryptionArr()
    data = ""
    for i in range(len(str)):
        if str[i] not in arr[0]:
            data += str[i]
            continue
        else:    
            index = arr[schemeNum].index(str[i])
            data += arr[0][index]   
    if data[len(data)-1] == '|':
        data = data.replace("|", "")
    return data
    
def TranspositionDecrypt(str):
# Cuts the plaintext into segments, each segment a string of r x n characters
    retStr = ''
    size, iter = numOfSegments(str)
    arrSize = size*size
    # Puts the string of characters into an r x n array A
    for i in range(iter):
        if i == iter:
            smallString = str[i*arrSize : len(str)-1]
        else:
            smallString = str[i*arrSize : (i+1)*arrSize]
            
        retStr += readArr(rearrageString(smallString, size))
    # Reads the array from top to bottom and columns from left to right.
    return retStr    

#########################################
### Helper functinos for tranposition ###     
#########################################

def numOfSegments(str):
# if length is less than 16 divide into 2x2 or 3x3, else return 4x4 and number of 
# segments.
# returns n (for nxn array) and number of segments needed
    length = len(str)
    if length < 2:
        return 0, 0
    elif length < 5: 
        return 2, 1
    elif length < 10:
        return 3, 1
    else:
        div = divmod(length, 16)
        if div[1] == 0:
            return 4, div[0]
        else:
            return 4, div[0]+1
       
def rearrageString(str, size):
# Returns string that has gone through transposition encryption 
    arr = [[]]
    for i in range(size-1):
        arr.append([])
        
    # Adds filler characters if smaller than array size        
    arrSize = size*size
    if arrSize > len(str):
        diff = arrSize - len(str)
        for k in range(diff):
            str += '|'   
    # Puts string into array and reads top-down to left-right  
    for i in range(size):
        for j in range(size):
            strIndex = i*size + j
            arr[j].append(str[strIndex]) 
    return arr
 
def readArr(arr):
    newStr = ''
    size = len(arr)
    for i in range(size):
        for j in range(size):
            newStr += arr[i][j]
    
    return newStr
     
#############################################################################
### Helper functions (for TextFrequency.py) to count frequency of letters ###
#############################################################################

def countLetters(str):    
    arr = initDecryptionArr()[0]
    countTracker = []
    for i in range(66):
        countTracker.append(0)
    for i in str:
        if i in arr:
            index = arr.index(i)
            countTracker[index] += 1
            
    displayLetterCount(arr, countTracker)
            
def displayLetterCount(letterNumberingArr, countArr):
    jump = False
    topFiveArr = []
    sortList = []
    for i in range(len(countArr)):
        sortList.append(countArr[i])
    
    sortList.sort()
    maxIndex = len(countArr)
    
    for i in range(5):
        index = countArr.index(sortList[maxIndex-1-i])
        topFiveArr.append([letterNumberingArr[index], countArr[index]])

    for i in range(len(topFiveArr)):
        print("character " + topFiveArr[i][0] + " has appeared: " + str(topFiveArr[i][1]) + " times")
        
def getText(name):
    string = ''
    with open(name, 'r') as file:
        for line in file:
            string += line
    return string
    
##################################################################
### functions to help initialize encryption/decryption schemes ###
##################################################################
 
def initDecryptionArr():
    encryptArr = initEncryptArr()
    arr = [encryptArr[0], [], [], []]
    for i in range(1,4):
        for j in range(66):
            arr[i].append(0)
    for i in range(1,4):
        for j in range(66):
            index = encryptArr[i].index(encryptArr[0][j])
            arr[i][index] = arr[0][j]
    return arr
    
def initEncryptArr():
# creates an array representing the substitution scheme
# 0-9 = 0, 1, ... ,9
# 10-35 = a, b, ... ,z
# 36-61 = A, B, ... , Z
# 62 = ' ', 63 = ',', 64 = '.', 65 = '?' 
    arr = [[], [], [], []]
    for i in range(4):
        for j in range(66):
            arr[i].append(0)
            
################## Start of creating schemes (CAN IGNORE) ##########################
# Original characters to index assignment  
    arr[0][0] = '0'
    arr[0][1] = '1'
    arr[0][2] = '2'
    arr[0][3] = '3'
    arr[0][4] = '4'
    arr[0][5] = '5'
    arr[0][6] = '6'
    arr[0][7] = '7'
    arr[0][8] = '8' 
    arr[0][9] = '9'
    arr[0][10] = 'a'
    arr[0][11] = 'b' 
    arr[0][12] = 'c'
    arr[0][13] = 'd'
    arr[0][14] = 'e'
    arr[0][15] = 'f'
    arr[0][16] = 'g'
    arr[0][17] = 'h' 
    arr[0][18] = 'i'
    arr[0][19] = 'j'
    arr[0][20] = 'k'
    arr[0][21] = 'l'
    arr[0][22] = 'm'
    arr[0][23] = 'n'
    arr[0][24] = 'o'
    arr[0][25] = 'p'
    arr[0][26] = 'q'
    arr[0][27] = 'r'
    arr[0][28] = 's'
    arr[0][29] = 't'
    arr[0][30] = 'u'
    arr[0][31] = 'v'
    arr[0][32] = 'w'
    arr[0][33] = 'x' 
    arr[0][34] = 'y' 
    arr[0][35] = 'z'
    arr[0][36] = 'A'
    arr[0][37] = 'B'
    arr[0][38] = 'C'
    arr[0][39] = 'D'
    arr[0][40] = 'E'
    arr[0][41] = 'F'
    arr[0][42] = 'G'
    arr[0][43] = 'H'
    arr[0][44] = 'I'
    arr[0][45] = 'J'
    arr[0][46] = 'K'
    arr[0][47] = 'L'
    arr[0][48] = 'M'
    arr[0][49] = 'N'
    arr[0][50] = 'O'
    arr[0][51] = 'P'
    arr[0][52] = 'Q'
    arr[0][53] = 'R'
    arr[0][54] = 'S'
    arr[0][55] = 'T'
    arr[0][56] = 'U'
    arr[0][57] = 'V'
    arr[0][58] = 'W'
    arr[0][59] = 'X'
    arr[0][60] = 'Y'
    arr[0][61] = 'Z'
    arr[0][62] = ' '
    arr[0][63] = ','
    arr[0][64] = '.'
    arr[0][65] = '?'
# 1st encryption scheme
    arr[1][0] = 'i'
    arr[1][1] = 'q'
    arr[1][2] = 'G'
    arr[1][3] = 'x'
    arr[1][4] = '0'
    arr[1][5] = 'a' 
    arr[1][6] = 'O'
    arr[1][7] = 'y'
    arr[1][8] = 'b' 
    arr[1][9] = 'W'
    arr[1][10] = 'j'
    arr[1][11] = '1'
    arr[1][12] = 'r'
    arr[1][13] = '9'
    arr[1][14] = 'H'
    arr[1][15] = '2'
    arr[1][16] = 'P'
    arr[1][17] = 'c' 
    arr[1][18] = 'X'
    arr[1][19] = 'k'
    arr[1][20] = 'z'
    arr[1][21] = 'Y'
    arr[1][22] = 'A'
    arr[1][23] = 'd'
    arr[1][24] = 'Q'
    arr[1][25] = 's'
    arr[1][26] = '3'
    arr[1][27] = 'I'
    arr[1][28] = 'l'
    arr[1][29] = 'Z'
    arr[1][30] = 'R'
    arr[1][31] = 'B'
    arr[1][32] = '4'
    arr[1][33] = 'e' 
    arr[1][34] = ' ' 
    arr[1][35] = 'm'
    arr[1][36] = 'J'
    arr[1][37] = 't'
    arr[1][38] = 'f'
    arr[1][39] = '.'
    arr[1][40] = '5'
    arr[1][41] = 'S'
    arr[1][42] = 'K'
    arr[1][43] = 'C'
    arr[1][44] = ','
    arr[1][45] = 'n'
    arr[1][46] = '?'
    arr[1][47] = 'L'
    arr[1][48] = '6'
    arr[1][49] = 'g'
    arr[1][50] = 'T'
    arr[1][51] = 'D'
    arr[1][52] = 'u'
    arr[1][53] = 'U'
    arr[1][54] = 'M'
    arr[1][55] = '7'
    arr[1][56] = 'o'
    arr[1][57] = 'V'
    arr[1][58] = 'E'
    arr[1][59] = 'h'
    arr[1][60] = 'v'
    arr[1][61] = 'N'
    arr[1][62] = 'F'
    arr[1][63] = 'w'
    arr[1][64] = 'p'
    arr[1][65] = '8'
# 2nd encryption scheme
    arr[2][1] = 'i'
    arr[2][2] = 'q'
    arr[2][3] = 'G'
    arr[2][4] = 'x'
    arr[2][5] = '0'
    arr[2][6] = 'a' 
    arr[2][7] = 'O'
    arr[2][8] = 'y'
    arr[2][9] = 'b' 
    arr[2][10] = 'W'
    arr[2][11] = 'j'
    arr[2][12] = '1'
    arr[2][13] = 'r'
    arr[2][14] = '9'
    arr[2][15] = 'H'
    arr[2][16] = '2'
    arr[2][17] = 'P'
    arr[2][18] = 'c' 
    arr[2][19] = 'X'
    arr[2][20] = 'k'
    arr[2][21] = 'z'
    arr[2][22] = 'Y'
    arr[2][23] = 'A'
    arr[2][24] = 'd'
    arr[2][25] = 'Q'
    arr[2][26] = 's'
    arr[2][27] = '3'
    arr[2][28] = 'I'
    arr[2][29] = 'l'
    arr[2][30] = 'Z'
    arr[2][31] = 'R'
    arr[2][32] = 'B'
    arr[2][33] = '4'
    arr[2][34] = 'e' 
    arr[2][35] = ' ' 
    arr[2][36] = 'm'
    arr[2][37] = 'J'
    arr[2][38] = 't'
    arr[2][39] = 'f'
    arr[2][40] = '.'
    arr[2][41] = '5'
    arr[2][42] = 'S'
    arr[2][43] = 'K'
    arr[2][44] = 'C'
    arr[2][45] = ','
    arr[2][46] = 'n'
    arr[2][47] = '?'
    arr[2][48] = 'L'
    arr[2][49] = '6'
    arr[2][50] = 'g'
    arr[2][51] = 'T'
    arr[2][52] = 'D'
    arr[2][53] = 'u'
    arr[2][54] = 'U'
    arr[2][55] = 'M'
    arr[2][56] = '7'
    arr[2][57] = 'o'
    arr[2][58] = 'V'
    arr[2][59] = 'E'
    arr[2][60] = 'h'
    arr[2][61] = 'v'
    arr[2][62] = 'N'
    arr[2][63] = 'F'
    arr[2][64] = 'w'
    arr[2][65] = 'p'
    arr[2][0] = '8'
# 3rd encryption scheme  
    arr[3][0] = 'i'
    arr[3][9] = 'q'
    arr[3][8] = 'G'
    arr[3][7] = 'x'
    arr[3][6] = '0'
    arr[3][5] = 'a' 
    arr[3][4] = 'O'
    arr[3][3] = 'y'
    arr[3][2] = 'b' 
    arr[3][1] = 'W'
    arr[3][10] = 'j'
    arr[3][19] = '1'
    arr[3][18] = 'r'
    arr[3][17] = '9'
    arr[3][16] = 'H'
    arr[3][15] = '2'
    arr[3][14] = 'P'
    arr[3][13] = 'c' 
    arr[3][12] = 'X'
    arr[3][11] = 'k'
    arr[3][20] = 'z'
    arr[3][29] = 'Y'
    arr[3][28] = 'A'
    arr[3][27] = 'd'
    arr[3][26] = 'Q'
    arr[3][25] = 's'
    arr[3][24] = '3'
    arr[3][23] = 'I'
    arr[3][22] = 'l'
    arr[3][21] = 'Z'
    arr[3][30] = 'R'
    arr[3][39] = 'B'
    arr[3][38] = '4'
    arr[3][37] = 'e' 
    arr[3][36] = ' ' 
    arr[3][35] = 'm'
    arr[3][34] = 'J'
    arr[3][33] = 't'
    arr[3][32] = 'f'
    arr[3][31] = '.'
    arr[3][40] = '5'
    arr[3][49] = 'S'
    arr[3][48] = 'K'
    arr[3][47] = 'C'
    arr[3][46] = ','
    arr[3][45] = 'n'
    arr[3][44] = '?'
    arr[3][43] = 'L'
    arr[3][42] = '6'
    arr[3][41] = 'g'
    arr[3][50] = 'T'
    arr[3][59] = 'D'
    arr[3][58] = 'u'
    arr[3][57] = 'U'
    arr[3][56] = 'M'
    arr[3][55] = '7'
    arr[3][54] = 'o'
    arr[3][53] = 'V'
    arr[3][52] = 'E'
    arr[3][51] = 'h'
    arr[3][60] = 'v'
    arr[3][65] = 'N'
    arr[3][64] = 'F'
    arr[3][63] = 'w'
    arr[3][62] = 'p'
    arr[3][61] = '8'
    
#######################################################################
################## End of creating schemes ############################
####################################################################### 
    
    return arr
