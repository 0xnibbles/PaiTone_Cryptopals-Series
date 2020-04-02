import string
from challenge2 import hex2bytes
from challenge3 import singleXOR, stringScore, charFrequency


def detect_SingleXOR(possibleStrings):

    xorString = ''
    maxScore = 0

    for msg in possibleStrings.keys():

        xorScore = stringScore(msg)


        if xorScore > maxScore:
            maxScore = xorScore
            xorString = msg


    return xorString

def main():

    with open("4.txt") as file:

        possibleStrings = {}

        for input in file:

            input = input.strip('\n')
            bytes = hex2bytes(input)

            string,letter = singleXOR(bytes)

            possibleStrings[string] = input

        msg = detect_SingleXOR(possibleStrings)

        print("Message: "+msg+"\nString: "+possibleStrings[msg])

if __name__ == "__main__":
    main()
