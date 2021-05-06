# Given string was encrypted using rot13. It can be done by hand (shifting each letter by 13 places) but I used a python program

import codecs
s = input("Given string: ")
print(codecs.encode(s, "rot_13"))

# Visit stackoverflow for more methods.
