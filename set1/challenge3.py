import string
from binascii import hexlify, unhexlify
from challenge2 import hex2bytes

## The best approach to count char frequency
# give score to spaces is not cheating right????

# some python functions such as map, lambda and max .....


def validChars():
    chars = string.ascii_letters + " "
    return chars

def charFrequency(letter):


    frequencyTable ={
        'A': 0.0651738,
        'B': 0.0124248,
        'C': 0.0217339,
        'D': 0.0349835,
        'E': 0.1041442,
        'F': 0.0197881,
        'G': 0.0158610,
        'H': 0.0492888,
        'I': 0.0558094,
        'J': 0.0009033,
        'K': 0.0050529,
        'L': 0.0331490,
        'M': 0.0202124,
        'N': 0.0564513,
        'O': 0.0596302,
        'P': 0.0137645,
        'Q': 0.0008606,
        'R': 0.0497563,
        'S': 0.0515760,
        'T': 0.0729357,
        'U': 0.0225134,
        'V': 0.0082903,
        'W': 0.0171272,
        'X': 0.0013692,
        'Y': 0.0145984,
        'Z': 0.0007836,
        ' ': 0.1918182 # is this the right thing to do with spaces?????
    }

    letterFrequency = frequencyTable.get(letter,0)

    return letterFrequency


def stringScore(string):

    totalScore = 0

    for letter in string:                   
        
        if letter in str(validChars()): # check if string has a "human" readble char

            charScore = charFrequency(letter.upper()) #char frequency dict is in uppercase          
            totalScore += charScore

    return totalScore


def singleXOR(bytes1):
    
    xorKey = ''
    maxScore = 0

    for key in range(256): # iterating over the 255 ascii characters

        xor = ''.join(chr(byte ^ key) for byte in bytes1)

        xorScore = stringScore(xor) 
        
        if xorScore > maxScore:
            maxScore = xorScore
            xorKey = chr(key)
            xorString = xor

    return xorString, xorKey


def main():
    input = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

    bytes = hex2bytes(input)

    msg,key = singleXOR(bytes)

    print("Message: "+msg+"\nKey: "+key)


if __name__ == "__main__":
    main()
