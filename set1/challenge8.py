import base64
from challenge3 import stringScore
from challenge6 import hammingDistance
import pprint


#testing approach
def detect_AES_ECB(ciphertext_list):

    ct_blocks = {}
    for j in range(0,len(ciphertext_list)):
        print(j)
        print("alala")
        ct_blocks[j] = 0
        for ct in ciphertext_list:
            repeated_Blocks = []
            ct_score = 0
            for i in range(0,len(ct),16):
                block = ct[i:i+16]
                #print(block)
                
                if block in repeated_Blocks:
                    #repeated_Blocks[block] +=1
                    ct_score += 1
                    ct_blocks[j] +=1
                    print("entraaaaaaaaaa")
                    print(ct_blocks[j])
                else:
                    repeated_Blocks.append(block)
        #ct_blocks[j] = ct_score
        #print(ct_score)
        #print(ct_blocks)

    #ct_ECB_index = sorted(ct_blocks, key=lambda x: ct_blocks[x], reverse=True)[0]
    #print(ciphertext_list[ct_ECB_index])
    print(ct_blocks)
        


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