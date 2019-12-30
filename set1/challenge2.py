import base64
from binascii import hexlify, unhexlify

#result = hex(0x1c0111001f010100061a024b53535009181c ^ 0x686974207468652062756c6c277320657965)

#print(result)

def hex2bytes(input):

    #return bytearray.fromhex(input) # direct conversion
    return bytes(int(''.join(c), 16) for c in zip(input[0::2],input[1::2])) # built another way to convert hex to bytes

def fixedXOR(bytes1,bytes2):
    
    # Iterating each byte over both byte arrays and do a XOR operation.
    # Return as a byte array

    if len(bytes1) != len(bytes2):
        raise ValueError('Strings must be equal length')

    xor = bytes((char1 ^ char2) for char1,char2 in zip(bytes1,bytes2))

    return xor


def main():
    
    input1 = "1c0111001f010100061a024b53535009181c"

    input2 = "686974207468652062756c6c277320657965"

    bytes1 = hex2bytes(input1)
    bytes2 = hex2bytes(input2)

    output = fixedXOR(bytes1,bytes2)

    print(hexlify(output)) # output the result as hexadecimal

    

if __name__ == "__main__":
    main()

