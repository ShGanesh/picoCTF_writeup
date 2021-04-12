'''
So the problem lies with the binary file. On decompiling file with Ghidra we can see this weird code chunk:

local_54 = 6;
while (local_54 < 0xf) {
    fputc((int)(char)(local_38[local_54] + '\x05'),__stream_00);
    local_54 = local_54 + 1;
 }
 fputc((int)(char)(local_29 + -3),__stream_00);
 local_50 = 0x10;
 while (local_50 < 0x1a) {
    fputc((int)local_38[local_50],__stream_00);
    local_50 = local_50 + 1;
 }

'''

# Understanding the assembly code:
'''
local_54, local_50 are nothing but variables.
I will now convert the above code in some sort of hybridized english-c-python. So in a way, we can understand the code as:
        s = {required_flag}
        characters 0 to 5:
                are left as it is
                not even mentioned here
        
        local_54 = 6                    (0x6 = 6)
        while (local_54 < 0xf):         (0xf = 16), characters 6 to 14
                hex value + 5
                local_54 += 1
        
        one character:                  (character 15)
                hex value - 3
        
        local_50 = 0x10                 (0x10 = 16)
        while (local_50 < 0x1a):        (0x1a = 26), characters 16 to 
                left as it is
                local_50 += 1

So we need to revert these changes. You can do it by hand if you want, but personally i'd rather try automating a 15 min task for 3 hours.
'''

# To solve, the picture was analysed using GHex and the hex values of the flag (which was present after IEND) were taken into an array beforehand.

hexes = "70 69 63 6f 43 54 4b 80 6b 35 7a 73 69 64 36 71 5f 64 31 64 65 65 64 61 61 7d"
l2 = tuple(hexes.split())                                               # Yes too many variables can be made more efficient.
# Converting Hex to ASCII
l = tuple(map(lambda x: int(x, 16), l2))
# Printing stuff because why not?
print('ASCII:', l)
print('Text:', end=' ')

for i in l:
	print(chr(i), end='')           
print('')
        
        
for i in range(6):			# picoCT,       the innocent stuff
	print(chr(l[i]), end='')
for i in range(6, 15):			# F{f0und_i,    was increased by 5
	print(chr(l[i]-5), end='')
print(chr(l[15]+3), end='')		# t,            was decreased by 3
for i in range(16, 26):
	print(chr(l[i]), end='')	# d1deedaa}     more innocent stuff
print ('')

