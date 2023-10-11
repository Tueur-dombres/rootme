from pwn import * # pip install pwntools
import json
import math
import codecs
import zlib

dico_morse = { 'A':'.-', 'B':'-...',
                'C':'-.-.', 'D':'-..', 'E':'.',
                'F':'..-.', 'G':'--.', 'H':'....',
                'I':'..', 'J':'.---', 'K':'-.-',
                'L':'.-..', 'M':'--', 'N':'-.',
                'O':'---', 'P':'.--.', 'Q':'--.-',
                'R':'.-.', 'S':'...', 'T':'-',
                'U':'..-', 'V':'...-', 'W':'.--',
                'X':'-..-', 'Y':'-.--', 'Z':'--..',
                '1':'.----', '2':'..---', '3':'...--',
                '4':'....-', '5':'.....', '6':'-....',
                '7':'--...', '8':'---..', '9':'----.',
                '0':'-----', ', ':'--..--', '.':'.-.-.-',
                '?':'..--..', '/':'-..-.', '-':'-....-',
                '(':'-.--.', ')':'-.--.-'}
dico_morse = {e:k for k,e in dico_morse.items()}

r = remote('challenge01.root-me.org', 52017)
for i in range(100):
    rcv=r.recv()
    print(rcv)

    ret = str(rcv).split()[-2][1:-5]
    print(ret)

    if sum(1 for e in ret if e not in "./-")==0:
        "morse !"
        ret = "".join(dico_morse[e] for e in ret.split("/")).lower()
    elif sum(1 for e in ret if e not in "".join(chr(i) for i in range(ord("A"),ord("Z")+1))+"23456=")==0:
        print("base 32 !")
        ret = base64.b32decode(ret).decode()
    elif sum(1 for e in ret if e not in "".join(chr(i) for i in range(ord("a"),ord("f")+1))+"0123456789")==0:
        print("hexadécimal !")
        ret = bytes.fromhex(ret).decode()
    elif sum(1 for e in ret if e not in "".join(chr(i) for i in range(ord("A"),ord("Z")+1))+"".join(chr(i) for i in range(ord("a"),ord("z")+1))+"0123456789=")==0:
        print("base 64 !")
        ret = base64.b64decode(ret).decode()
    elif sum(1 for e in ret if e not in "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!#$%&()*+-;<=>?@^_`{|}~")==0:
        print("base 85 !")
        ret = base64.b85decode(ret).decode()
    
    print(ret)
    r.send((str(ret) + "\n").encode())
rcv=r.recv()
print(rcv)