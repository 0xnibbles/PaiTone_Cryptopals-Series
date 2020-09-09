import base64
from challenge6 import hammingDistance
import pprint


#testing approach
def detect_AES_ECB(ciphertext):

    repeated_Blocks = {}

    #print(ciphertext)
    k=0
    for i in range(0,len(ciphertext),16):
        block = ciphertext[i:i+16]
        #print(block)
        if block in repeated_Blocks:
            repeated_Blocks[block] +=1
        else:
            repeated_Blocks[block] = 1
    
    pprint.pprint(repeated_Blocks)

def main():
    input =""
    ciphertext= ""
    with open("7.txt") as file:
        for line in file:
            input += line.strip("\n")
    ciphertext = input.encode()
    #print(ciphertext)
    detect_AES_ECB(ciphertext)


if __name__ == "__main__":
    main()