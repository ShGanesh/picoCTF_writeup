from pwn import *

conn = remote('jupiter.challenges.picoctf.org', 15130)

# first binary
_ = conn.recvregex('Please give the ')
b = conn.recvregex(' as a word.')
s = b.decode('utf-8')


string = s[:-11]
plaintext = "".join([chr(int(binary, 2)) for binary in string.split(" ")])
_ = conn.recvregex("Input:\n")
conn.sendline(plaintext)

# now Octal
_ = conn.recvregex('Please give me the  ')
b = conn.recvregex(' as a word.')
s = b.decode('utf-8')[:-11]
plaintext = ""
for x in s.split(" "):
	plaintext += chr(int(x, 8))
_ = conn.recvregex("Input:\n")
conn.sendline(plaintext)

# now Hex
b = conn.recvuntil(".")
s = b.decode('utf-8')
ans = bytes.fromhex(s.split()[4])
plaintext = ans.decode("ASCII")
conn.sendline(plaintext)

# get flag
_ = conn.recvline()

conn.interactive()


# If it gets stuck do ctrl+c.
# You will get the answer nonetheless.
