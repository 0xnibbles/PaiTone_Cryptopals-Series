
import binascii

def ascii2bin(s):
    return bin(int(binascii.hexlify(s),16)) 
    

def hammingDistance(s1,s2):

    if len(s1) != len(s2):
        raise ValueError('Strings must be equal length')
    
    return sum(c1 !=c2 for c1,c2 in zip(s1,s2))


'''
def break_RepeatingXOR:

    for keySize in range(2,40,2):
'''


def main():

    s1 = "this is a test".encode()
    s2 = "wokka wokka!!!".encode()

    hammingDistance(ascii2bin(s1),ascii2bin(s2))

    with open("6.txt") as file:

        possibleStrings = {}

        for input in file:

            input = input.strip('\n')

            ## breaking repeating xor....

if __name__ == "__main__":
    main() 