import binascii 
from binascii import hexlify
import sys

def repeated_KeyXOR(s,key):

    return bytes(s[i] ^ key[i % len(key)] for i in range(max(len(s),len(key)))) # using a circular key
    

def main():

    if len(sys.argv) < 2:
        input = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal".encode() #convert ascii to bytes
    else:
        input = sys.argv[1].encode()
    print(input)
    key = "ICE".encode()
    
    msg = repeated_KeyXOR(input,key)

    print("Message: "+str(hexlify(msg)))
    

if __name__ == "__main__":
    main() 