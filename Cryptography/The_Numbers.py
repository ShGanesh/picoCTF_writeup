l = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# Hint: format is fully in CAPS.


n = "<Space separated characters taken from that .png>"

a = ""
for i in n.split():
	if i.isnumeric():
			a += l[int(i)-1]
	else:
		a += i
print(a)

