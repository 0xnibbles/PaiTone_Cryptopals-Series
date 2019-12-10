
import base64

input = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

decode_input = ''.join([chr(int(''.join(c), 16)) for c in zip(input[0::2],input[1::2])]);

b64_string = base64.b64encode(str.encode(decode_input))

#b64_string = base64.b64encode(bytes(bytearray.fromhex(input).decode(),"utf-8")) # another way of converting hex to b64


print(b64_string)