import base64
from challenge3 import stringScore
from challenge6 import hammingDistance
import pprint


#testing approach
def detect_AES_ECB(ciphertext_list):

    repeated_Blocks = {}

    ct_blocks = {}
    #print(ciphertext)
    k=0
    j= -1
    
    for ct in ciphertext_list:
        j=j+1
        ct_blocks[j] = 0
        ct_score = 0
        s1 = b""
        s2 = b""
        for i in range(0,len(ct),16):
            block = ct[i:i+16]
            #print(block)
            '''
            if block in repeated_Blocks:
                repeated_Blocks[block] +=1
            else:
                repeated_Blocks[block] = 1
            '''
            s2 = block
            #print(s1)
            if s1 != b"":
                #ct_score += stringScore(block)
                ct_score += hammingDistance(s1,s2) # less distance = more equal
                #print(ct_score)

            s1 = s2

        ct_blocks[j] = ct_score

    ct_ECB_index = sorted(ct_blocks, key=lambda x: ct_blocks[x], reverse=True)[0]
    print(ciphertext_list[ct_ECB_index])
    #print(sorted(ct_blocks, key=lambda x: ct_blocks[x], reverse=True))

def main():
    input =""
    ciphertext= []
    with open("8.txt") as file:
        for line in file:
            ciphertext.append(line.strip("\n").encode())
        #content = [line.strip("\n") for line in file]
    #print(content)
    #ciphertext = input.encode()
    #pprint.pprint(ciphertext[:12])
    detect_AES_ECB(ciphertext)

    


if __name__ == "__main__":
    main()