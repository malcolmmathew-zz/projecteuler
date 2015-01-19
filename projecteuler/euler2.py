x = 1
y = 2
d= 2
for a in range(0,4000):
	z = x+y
	if z>4000000:
		break
	if z%2 ==0:
		d += z
	x=y
	y=z
print d