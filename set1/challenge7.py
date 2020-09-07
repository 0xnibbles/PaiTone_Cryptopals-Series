from Crypto.Cipher import AES
import base64



def main():
    
    input= ""
    ciphertext= ""
    with open("7.txt") as file:
        for line in file:
            input+= line.strip("\n")
    ciphertext = base64.b64decode(input)
    
    key = "YELLOW SUBMARINE"
    cipher = AES.new(key.encode(), AES.MODE_ECB) # the key must be in bytes
    plaintext = cipher.decrypt(ciphertext)

    print(plaintext.decode()) # print as ASCII




if __name__ == "__main__":
    main()