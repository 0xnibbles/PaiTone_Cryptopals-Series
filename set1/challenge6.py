
import binascii
import base64
from challenge2 import hex2bytes
from challenge3 import singleXOR

keyMaxSize=40 # possible max key size

def hex2bin(s):

    return bin(int(binascii.hexlify(s),16))
    

def hammingDistance(s1, s2):

    if len(s1) != len(s2):
        ValueError('Values must be equal length')

    #XORing each block results to 1's be different and 0's to be equal bits
    distance = bin(int(binascii.hexlify(s1),16) ^ int(binascii.hexlify(s2),16)).count("1")
    return distance


def get_probable_key_size(cipher): # smallest key size values
    
    if keyMaxSize >= len(cipher)//4:
        raise ValueError('Key Max Size length can\'t be lower of half the ciphertext')

    fcb = "" # first cipher bytes
    scb = "" # second cipher bytes
    tcb = "" # third cipher bytes
    qcb = "" # quarter cipher bytes

    normalizedHammingDistance = {}

    for keySize in range(2,keyMaxSize):
        
        fcb = cipher[:keySize]
        scb = cipher[keySize:len(cipher)-(len(cipher)-(2*keySize))] # or cipher[keySize : 2*keySize]
        tcb = cipher[2*keySize:len(cipher)-(len(cipher)-(3*keySize))]
        qcb = cipher[3*keySize:len(cipher)-(len(cipher)-(4*keySize))]

        #print(str(keySize)+" --------------------------------")

        # normalizing each hamming distance and get arithmetic mean
        normalizedHammingDistance[keySize] = (hammingDistance(fcb,scb)+ hammingDistance(scb,tcb) + \
            hammingDistance(tcb,qcb)) / (keySize * 3) 
    
    # sorting by the lowest hamming distance and get each respective key
    problable_keysizes = {values: keys for values, keys in sorted(normalizedHammingDistance.items(), key=lambda value: value[1])[:4]}
    
    #print(problable_keysizes)
    return problable_keysizes.keys()
    

def cipherBlocks(guess_keys,cipher):

    blocks ={}
    block =""
    
    for keySize in guess_keys:                    # iterate each key
        blocks[keySize] = []
        
        for k in range(0,len(cipher),keySize):    # split cipher blocks by key size
            block_bytes = b''
            for i in range(k,k):
                block_bytes +=bytes([cipher[i]])
                #block_bytes += bcipher[k]
                #print(block)
            blocks[keySize].append(block_bytes)
        #key_blocks.append(blocks)

    print(len(blocks[2]))
    return blocks
    
def break_repeating_keyXor(blocks):
    
    for bytes_blocks in blocks:
        #print(bytes_blocks)
        msg, key = singleXOR(bytes_blocks)
        #print(key+": "+msg)

def main():

    s1 = "this is a test".encode()
    s2 = "wokka wokka!!!".encode()
    #print(hammingDistance(s1,s2))
    
    with open("6.txt") as file:

        cipher = ""
        for input in file:
            cipher += input.strip('\n')
        cipher = base64.b64decode(cipher)
        

        ## breaking repeating xor....
        guess_keys = get_probable_key_size(cipher)
        blocks = cipherBlocks(guess_keys,cipher)
        #print(blocks[0])
        #break_repeating_keyXor(blocks)

if __name__ == "__main__":
    main() 