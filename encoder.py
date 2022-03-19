import sys
import base64
import pyperclip
from hashlib import blake2b

#blake2b da dodam
encoders = ('base64', 'blake2b')

def encode_str(enc):
    if enc == 'base64':
        return base64.b64encode(bytes(sys.argv[2], 'utf-8'), altchars=None).decode('utf-8')
    if enc == 'blake2b':
        blake = blake2b()
        blake.update(bytes(sys.argv[2], 'utf-8'))
        return blake.digest()
    else:
        print(f'[+] Usage: python {sys.argv[0]} [encoding] [string] - encode a string')



if len(sys.argv) < 3:
    print('[+] Missing an argument')
    print(f'[+] Usage: python {sys.argv[0]} [encoding] [string] - encode a string')
    sys.exit()
elif sys.argv[1] not in encoders:
        print(f'[+] Encoding type not supported')
        print('[+] Supported types: base64, blake2b.')
        print(f'[+] Usage: python {sys.argv[0]} [encoding] [string] - encode a string')
else:
    pyperclip.copy(str(encode_str(sys.argv[1])))
    print('[+] Encoded string has been copied to your clipboard !')
    print(f'[+] Encoding type : {sys.argv[1]}')





#sys argv da omogucim cak i ako se koristi space nekako for sys.argv[i] += sys.argv[i] taj neki fazon(nema potrebe ipak)