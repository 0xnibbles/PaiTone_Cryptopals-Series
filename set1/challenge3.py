import base64

def raw_bytes(input): 
    
    bytes = ''

    for byte in zip(input[0::2], input [1::2]): # read a byte from input
        bytes += chr(int(''.join(byte),16))
        
    return bytes

def bytes2b64(bytes):

    b64encode = base64.b64encode(str.encode(bytes))

    return b64encode

def charFrequency(letter):

    frequencyTable ={
        'E' : 12.0,
        'T' : 9.10,
        'A' : 8.12,
        'O' : 7.68,
        'I' : 7.31,
        'N' : 6.95,
        'S' : 6.28,
        'R' : 6.02,
        'H' : 5.92,
        'D' : 4.32,
        'L' : 3.98,
        'U' : 2.88,
        'C' : 2.71,
        'M' : 2.61,
        'F' : 2.30,
        'Y' : 2.11,
        'W' : 2.09,
        'G' : 2.03,
        'P' : 1.82,
        'B' : 1.49,
        'V' : 1.11,
        'K' : 0.69,
        'X' : 0.17,
        'Q' : 0.11,
        'J' : 0.10,
        'Z' : 0.07
    }
    letterFrequency = frequencyTable.get(letter)
    return letterFrequency

def singleXOR(bytes):
    print(bytes)

    xor = ''.join(chr(byte ^ letter) for byte in bytes for letter in range(256))

    print(xor)
    

def main():
    input = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

    bytes = raw_bytes(input)

    singleXOR(bytes)

    #b64Input = bytes2b64(bytes)

    


if __name__ == "__main__":
    main()
