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
rcv=r.recv()
print(rcv)

ret = str(rcv).split()
print(ret)


print(ret)
r.send((str(ret) + "\n").encode())

rcv=r.recv()
print(rcv)