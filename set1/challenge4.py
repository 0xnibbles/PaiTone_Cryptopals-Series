from binascii import hexlify, unhexlify
from challenge2 import hex2bytes
from challenge3 import singleXOR, stringScore

def detect_SingleXOR(possibleStrings):

    xorString = ''
    maxScore = 0

    for msg in possibleStrings.keys():
        #print(msg)

        xorScore = stringScore(msg)

        print("---------------------")
        print(msg)
        print(xorScore)
        print("---------------------")

        if xorScore > maxScore:
            maxScore = xorScore
            xorString = msg


        #print(possibleStrings)
        #print(len(possibleStrings))
    #print(xorString)
    return xorString

def main():

    with open("4.txt") as file:

        possibleStrings = {}

        for input in file:
            
            bytes = hex2bytes(input)

            string,letter = singleXOR(bytes)

            possibleStrings[string] = input

        msg = detect_SingleXOR(possibleStrings)

        #msg,key = singleXOR(bytes)
        #print(possibleStrings.keys())

        #print("Message: "+msg+"\nString: "+possibleStrings[msg])

        


if __name__ == "__main__":
    main()
