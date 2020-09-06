
import binascii
import base64
from challenge2 import hex2bytes
from challenge3 import singleXOR, stringScore
from challenge5 import repeated_KeyXOR

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
    
    if keyMaxSize >= len(cipher)//4: # floor division
        raise ValueError('Key Max Size length can\'t be higher of a quarter half the ciphertext size')

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

        # normalizing each hamming distance and get arithmetic mean
        normalizedHammingDistance[keySize] = (hammingDistance(fcb,scb)+ hammingDistance(scb,tcb) + \
            hammingDistance(tcb,qcb)) / (keySize * 3) 
    
    # sorting by the lowest hamming distance and get each respective key
    problable_keysizes = {values: keys for values, keys in sorted(normalizedHammingDistance.items(), key=lambda value: value[1])[:4]}
    
    return list(problable_keysizes.keys()) # return key sizes as list
    
# int guess_keys | bytes cipher
def cipherBlocks(guess_keys,cipher):

    cipherText_blocks ={}
    transpose_blocks = {}
    transpose_cipher ={}
    block =""    
    
    for keySize in guess_keys:                    # iterate each key
        cipherText_blocks[keySize] = []
        transpose_cipher[keySize] = []
        transpose_blocks[keySize]= []
        lastIndex=0
        block=b''
        
        temp_blocks = [] # temporary list with block of each key
        for k in range(0,len(cipher)+1,keySize):    # split cipher blocks by key size | #+1 because range 2n parameter is exclusive
           
            block = bytes(cipher[lastIndex:k]) 
            transpose_block =b''
            
            for j in range(0,len(block)):

                if len(temp_blocks)-1 < j:
                    temp_blocks.append(bytes([block[j]])) # square brackets are important. check doc why
                else:
                    temp_blocks[j] = temp_blocks[j] + bytes([block[j]])   

            lastIndex = k # the reason for the +1 in the range condition "len(cipher)+1"

            ''' 
            -- Why not using len(cipher)? As range 2nd parameter is exclusive, block will contain chars
            from lastIndex to k-1. This means is possible the last byte of the ciphertext to not be added to temp_blocks.
            Using len(cipher)+1, the range will be until to the last byte of ciphertext
            as is going to be -> (len(cipher) +1) -1(exclusive) = len(cipher), adding all the ct bytes

            '''
        transpose_blocks[keySize] = temp_blocks # dictionary with the respective list of block with their keys | key: keySize, value: key Size blocks
            
    return transpose_blocks



def find_keys(blocks):
    possible_keys=[]
    best_score =0
    key_xor = ""
    for key in blocks:
        xor_key = ""
        plaintext = ""
        for block in blocks[key]:
            msg, key = singleXOR(block)
            xor_key += key
            plaintext += msg
        possible_keys.append(xor_key)
    return possible_keys

def break_repeating_keyXor(ciphertext,possible_keys):

    score =0
    maxScore=0
    plaintext = ""
    cipher_key = ""
    for key in possible_keys:
        possible_plaintext = repeated_KeyXOR(ciphertext,key.encode()) # encoding key to XOR with ciphertext
        score = stringScore(possible_plaintext.decode()) # decoding because possible_plaintext is in bytes but stringScore uses ASCII chars
        if score > maxScore:
            maxScore = score
            plaintext = possible_plaintext.decode()
            cipher_key = key
    
    return cipher_key,plaintext

def main():

    s1 = "this is a test".encode()
    s2 = "wokka wokka!!!".encode()
    #print(hammingDistance(s1,s2)) # test if the hamming distance function
    
    with open("6.txt") as file:

        cipher = ""
        for input in file:
            cipher += input.strip('\n')
        cipher = base64.b64decode(cipher)        

        ## breaking repeating xor....
        guess_keys = get_probable_key_size(cipher)
        blocks = cipherBlocks(guess_keys,cipher)
        possibleKeys = find_keys(blocks)
        key,plaintext = break_repeating_keyXor(cipher,possibleKeys)

        print("Key: "+key+"\n\nOriginal Message:\n\n"+plaintext)

if __name__ == "__main__":
    main() 

