
'''
    According to the ECB mode, if there are identical blocks of plaintext, these will result in
    identical ciphertext blocks. So, the approach here is to detect which is the ciphertext
    where exists identical or equal blocks.
    The ciphertext with more equal blocks is more likely to be encrypted with AES-ECB
'''

def detect_AES_ECB(ciphertext_list):

    ct_blocks = {}
    
    for i in range(0,len(ciphertext_list)): # iterating each ciphertext

        ct = ciphertext_list[i] # selecting a ciphertext from the list
        
        repeated_Blocks = []    # list to save repeated blocks of each ciphertext
        ct_score = 0            # number of repeated blocks
        for j in range(0,len(ct),16):   # chunks of 16 bytes
            block = ct[j:j+16]          #  cyphertext block of 16 bytes
            
            if block in repeated_Blocks:    # if the block is already in the list it means a similar ciphertext has been appeared
                ct_score += 1
            else:
                repeated_Blocks.append(block)

        ct_blocks[i] = ct_score     # adding the number of repeated related to index of the ciphertext in the ciphertext_list

    ct_ECB_index = sorted(ct_blocks, key=lambda x: ct_blocks[x], reverse=True)[0] # sorting for the index with the most block reptitions in reverse order
    return ct_ECB_index, ct_blocks[ct_ECB_index]


def main():
    input =""
    ciphertext= []
    ecb_score = 0
    with open("8.txt") as file:
        for line in file:
            ciphertext.append(line.strip("\n").encode())
    
    aes_ecb_index, ecb_score = detect_AES_ECB(ciphertext)
    print("\nThe ciphertex encrypted with AES-ECB is:\n\n"+ciphertext[aes_ecb_index].decode())
    print("\nRepeated blocks: "+str(ecb_score))

if __name__ == "__main__":
    main()